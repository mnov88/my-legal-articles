import { App, Editor, MarkdownView, Modal, Notice, Plugin, PluginSettingTab, Setting } from 'obsidian';

interface FootnoteConverterSettings {
	moveToEof: boolean;
}

const DEFAULT_SETTINGS: FootnoteConverterSettings = {
	moveToEof: true
}

export default class FootnoteConverterPlugin extends Plugin {
	settings: FootnoteConverterSettings;

	async onload() {
		await this.loadSettings();

		// Command to convert footnotes in the current note
		this.addCommand({
			id: 'convert-footnotes-current-note',
			name: 'Convert footnotes in current note',
			editorCallback: (editor: Editor, view: MarkdownView) => {
				const content = editor.getValue();
				const converted = this.convertFootnotes(content, this.settings.moveToEof);
				editor.setValue(converted);
				new Notice('Footnotes converted!');
			}
		});

		// Command to open the conversion modal
		this.addCommand({
			id: 'open-footnote-converter-modal',
			name: 'Open footnote converter modal',
			callback: () => {
				new FootnoteConverterModal(this.app, this).open();
			}
		});

		// Add settings tab
		this.addSettingTab(new FootnoteConverterSettingTab(this.app, this));
	}

	convertFootnotes(text: string, moveToEof: boolean): string {
		// Step 1: Convert inline references to [^n] format
		// Handles marker-style: [1](#page-3-2) or [10\)](#page-2-1)
		// Handles Word-style: [[10]](#_ftn10)
		text = text.replace(/\[\[(\d+)\]\]\(#_ftn\d+\)/g, '[^$1]'); // Word format
		text = text.replace(/\[(\d+)\\?\]\(#[^\)]+\)/g, '[^$1]'); // Marker format
		
		// Step 2: Convert footnote definitions
		// Word-style: [[1]](#_ftnref1) Content → [^1]: Content
		text = text.replace(/\[\[(\d+)\]\]\(#_ftnref\d+\)\s+/g, '[^$1]: ');
		
		// Marker-style: <span id="..."></span><sup>1</sup> Content → [^$1]: Content
		text = text.replace(
			/<span id="[^"]+"><\/span>\s*<sup>(\d+)<\/sup>\s+/g,
			'[^$1]: '
		);
		
		// Step 3: Clean up any remaining isolated <sup> tags at start of lines (marker format)
		text = text.replace(/^<sup>(\d+)<\/sup>\s+/gm, '[^$1]: ');
		
		// Step 4: Remove standalone anchor spans (marker format - those not followed by <sup>)
		text = text.replace(/<span id="[^"]+"><\/span>(?!\s*<sup>)/g, '');
		
		// Step 5: Remove any remaining HTML tags (spans, anchors, etc.)
		text = text.replace(/<\/?span[^>]*>/g, '');
		text = text.replace(/<\/?a[^>]*>/g, '');
		
		// Step 6: Clean up multiple consecutive blank lines
		text = text.replace(/\n{3,}/g, '\n\n');
		
		// Step 7: Optionally move all footnotes to end of file
		if (moveToEof) {
			const footnotes: string[] = [];
			const footnotePattern = /^\[\^(\d+)\]:\s+.+$/gm;
			
			// Extract all footnote definitions
			let match;
			while ((match = footnotePattern.exec(text)) !== null) {
				footnotes.push(match[0]);
			}
			
			// Remove footnotes from original positions
			text = text.replace(footnotePattern, '').replace(/\n{3,}/g, '\n\n').trim();
			
			// Add footnotes at the end
			if (footnotes.length > 0) {
				text += '\n\n## Footnotes\n\n' + footnotes.join('\n\n');
			}
		}
		
		return text;
	}

	onunload() {
		// Cleanup if needed
	}

	async loadSettings() {
		this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
	}

	async saveSettings() {
		await this.saveData(this.settings);
	}
}

class FootnoteConverterModal extends Modal {
	plugin: FootnoteConverterPlugin;
	inputEl: HTMLTextAreaElement;
	outputEl: HTMLTextAreaElement;

	constructor(app: App, plugin: FootnoteConverterPlugin) {
		super(app);
		this.plugin = plugin;
	}

	onOpen() {
		const { contentEl } = this;
		
		contentEl.createEl('h2', { text: 'Footnote Converter' });
		
		// Description
		contentEl.createEl('p', { 
			text: 'Paste your markdown with HTML-style footnotes below and click Convert.',
			cls: 'setting-item-description'
		});

		// Input section
		contentEl.createEl('h3', { text: 'Input' });
		this.inputEl = contentEl.createEl('textarea', {
			placeholder: 'Paste your markdown here...',
			cls: 'footnote-converter-textarea'
		});
		this.inputEl.style.width = '100%';
		this.inputEl.style.height = '200px';
		this.inputEl.style.marginBottom = '1em';

		// Convert button
		const buttonContainer = contentEl.createDiv({ cls: 'footnote-converter-buttons' });
		buttonContainer.style.marginBottom = '1em';
		
		const convertBtn = buttonContainer.createEl('button', { text: 'Convert' });
		convertBtn.addEventListener('click', () => {
			const input = this.inputEl.value;
			const output = this.plugin.convertFootnotes(input, this.plugin.settings.moveToEof);
			this.outputEl.value = output;
		});

		// Output section
		contentEl.createEl('h3', { text: 'Output' });
		this.outputEl = contentEl.createEl('textarea', {
			placeholder: 'Converted markdown will appear here...',
			cls: 'footnote-converter-textarea'
		});
		this.outputEl.style.width = '100%';
		this.outputEl.style.height = '200px';
		this.outputEl.style.marginBottom = '1em';
		this.outputEl.readOnly = true;

		// Action buttons
		const actionContainer = contentEl.createDiv({ cls: 'footnote-converter-actions' });
		
		const copyBtn = actionContainer.createEl('button', { text: 'Copy to Clipboard' });
		copyBtn.addEventListener('click', () => {
			navigator.clipboard.writeText(this.outputEl.value);
			new Notice('Copied to clipboard!');
		});

		const insertBtn = actionContainer.createEl('button', { text: 'Insert into Current Note' });
		insertBtn.style.marginLeft = '0.5em';
		insertBtn.addEventListener('click', () => {
			const activeView = this.app.workspace.getActiveViewOfType(MarkdownView);
			if (activeView) {
				activeView.editor.replaceSelection(this.outputEl.value);
				new Notice('Inserted into note!');
				this.close();
			} else {
				new Notice('No active note found!');
			}
		});
	}

	onClose() {
		const { contentEl } = this;
		contentEl.empty();
	}
}

class FootnoteConverterSettingTab extends PluginSettingTab {
	plugin: FootnoteConverterPlugin;

	constructor(app: App, plugin: FootnoteConverterPlugin) {
		super(app, plugin);
		this.plugin = plugin;
	}

	display(): void {
		const { containerEl } = this;

		containerEl.empty();

		containerEl.createEl('h2', { text: 'Footnote Converter Settings' });

		new Setting(containerEl)
			.setName('Move footnotes to end of file')
			.setDesc('When enabled, all footnote definitions will be moved to a "Footnotes" section at the end of the document.')
			.addToggle(toggle => toggle
				.setValue(this.plugin.settings.moveToEof)
				.onChange(async (value) => {
					this.plugin.settings.moveToEof = value;
					await this.plugin.saveSettings();
				}));
	}
}
