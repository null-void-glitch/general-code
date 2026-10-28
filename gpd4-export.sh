#!/usr/bin/env bash
# Run on THIS machine. Creates ~/gpd4-dotfiles.tar.gz with everything the
# Pocket 4 setup script needs.
set -euo pipefail

OUT="$HOME/gpd4-dotfiles.tar.gz"
STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT

echo "Staging configs…"

# -- Hyprland (full dir except monitors.lua + plugins .so - rebuilt on target)
rsync -a --exclude="monitors.lua" --exclude="monitors.conf" \
         --exclude="plugins/*.so" \
         "$HOME/.config/hypr/" "$STAGE/hypr/"

# -- Quickshell ii config (user customizations live here)
rsync -a "$HOME/.config/quickshell/" "$STAGE/quickshell/"

# -- Kitty
rsync -a "$HOME/.config/kitty/" "$STAGE/kitty/"

# -- Oh-my-posh
rsync -a "$HOME/.config/ohmyposh/" "$STAGE/ohmyposh/"

# -- Zellij
rsync -a "$HOME/.config/zellij/" "$STAGE/zellij/"

# -- Cava
rsync -a "$HOME/.config/cava/" "$STAGE/cava/"

# -- Cava underlay config
rsync -a "$HOME/.config/hyprland-cava-underlay/" "$STAGE/hyprland-cava-underlay/"

# -- Theme switcher themes
rsync -a "$HOME/.config/theme-switcher/" "$STAGE/theme-switcher/"

# -- Zshrc + zshrc.d
cp "$HOME/.zshrc" "$STAGE/zshrc"
rsync -a "$HOME/.config/zshrc.d/" "$STAGE/zshrc.d/"

# -- theme-set script
cp "$HOME/.local/bin/theme-set" "$STAGE/theme-set"

# -- Wallpapers (skip heavy video/img thumbnails)
rsync -a --exclude="mpvpaper_thumbnails/" \
         --exclude="wallpaperengine_thumbnails/" \
         "$HOME/wallpapers/" "$STAGE/wallpapers/"

echo "Creating archive at $OUT…"
tar -czf "$OUT" -C "$STAGE" .
echo "Done. $(du -sh "$OUT" | cut -f1) → $OUT"
echo ""
echo "Transfer to Pocket 4:"
echo "  scp $OUT user@pocket4:~/"
echo "  # or: rsync -avP $OUT user@pocket4:~/"
