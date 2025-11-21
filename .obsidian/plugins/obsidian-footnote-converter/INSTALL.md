# Installation Guide for Footnote Converter Plugin

This guide will walk you through installing and setting up the Footnote Converter plugin for Obsidian.

## Prerequisites

- Obsidian app installed (version 0.15.0 or higher)
- For development: Node.js (v16 or higher) and npm

## Method 1: Manual Installation (Recommended for now)

### Step 1: Locate Your Vault's Plugin Folder

1. Open your Obsidian vault
2. Navigate to: `YourVault/.obsidian/plugins/`
   - On Windows: `C:\Users\YourName\Documents\YourVault\.obsidian\plugins\`
   - On Mac: `/Users/YourName/Documents/YourVault/.obsidian/plugins/`
   - On Linux: `/home/yourname/Documents/YourVault/.obsidian/plugins/`

### Step 2: Create Plugin Directory

Create a new folder called `footnote-converter` inside the `plugins` folder:
```
YourVault/.obsidian/plugins/footnote-converter/
```

### Step 3: Build the Plugin

Open a terminal in the plugin source directory and run:

```bash
# Install dependencies
npm install

# Build the plugin
npm run build
```

This will create:
- `main.js` - The compiled plugin code
- `manifest.json` - Plugin metadata
- `styles.css` - Plugin styles

### Step 4: Copy Files to Your Vault

Copy these three files to your vault's plugin folder:
```bash
cp main.js manifest.json styles.css /path/to/vault/.obsidian/plugins/footnote-converter/
```

Your folder structure should look like:
```
YourVault/
└── .obsidian/
    └── plugins/
        └── footnote-converter/
            ├── main.js
            ├── manifest.json
            └── styles.css
```

### Step 5: Enable the Plugin

1. Open Obsidian
2. Go to Settings (gear icon)
3. Click on "Community plugins"
4. If you see a warning about community plugins, click "Turn on community plugins"
5. Click "Reload plugins" or restart Obsidian
6. Find "Footnote Converter" in the list of installed plugins
7. Toggle it on

## Method 2: Development Installation

If you're actively developing the plugin:

### Step 1: Clone to Plugin Folder

Clone the repository directly into your vault's plugin folder:

```bash
cd /path/to/vault/.obsidian/plugins/
git clone https://github.com/yourusername/obsidian-footnote-converter.git footnote-converter
cd footnote-converter
```

### Step 2: Install and Build

```bash
npm install
npm run dev
```

The `npm run dev` command will watch for changes and automatically rebuild.

### Step 3: Enable in Obsidian

1. Open Obsidian Settings
2. Navigate to Community Plugins
3. Click "Reload plugins"
4. Enable "Footnote Converter"

### Step 4: Development Workflow

1. Make changes to `main.ts`
2. The plugin will automatically rebuild (if using `npm run dev`)
3. Reload Obsidian (Ctrl/Cmd + R) to see changes
4. Test your changes

## Verifying Installation

After enabling the plugin, verify it's working:

1. Open the command palette (Ctrl/Cmd + P)
2. Type "footnote"
3. You should see:
   - "Convert footnotes in current note"
   - "Open footnote converter modal"

## Troubleshooting

### Plugin Doesn't Appear in List

1. Check that files are in the correct location
2. Ensure all three files (main.js, manifest.json, styles.css) are present
3. Try restarting Obsidian completely
4. Check the developer console (Ctrl/Cmd + Shift + I) for errors

### Plugin Won't Enable

1. Check Obsidian version (needs 0.15.0+)
2. Verify manifest.json is valid JSON
3. Look for error messages in Settings → Community Plugins
4. Check developer console for errors

### Build Errors

```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Try building again
npm run build
```

### Plugin Not Working After Updates

1. Rebuild the plugin: `npm run build`
2. Copy new main.js to vault
3. Reload Obsidian: Ctrl/Cmd + R

## Updating the Plugin

### Manual Updates

1. Pull the latest changes:
   ```bash
   cd /path/to/plugin/source
   git pull
   ```

2. Rebuild:
   ```bash
   npm install
   npm run build
   ```

3. Copy files to vault (if not developing in plugin folder)

4. Reload Obsidian

### Automatic Updates (Once Published)

Once the plugin is in the community plugin store, updates will be managed through Obsidian's built-in update system.

## Uninstalling

1. Go to Settings → Community Plugins
2. Find "Footnote Converter"
3. Click the X or disable it
4. Delete the folder: `YourVault/.obsidian/plugins/footnote-converter/`

## Getting Help

- **GitHub Issues**: Report bugs or request features
- **Documentation**: See README.md for usage instructions
- **Community**: Join the Obsidian Discord or forum

## Next Steps

Once installed, check out:
- README.md for usage examples
- Settings to configure footnote placement
- The command palette for available commands

Happy converting! 📝
