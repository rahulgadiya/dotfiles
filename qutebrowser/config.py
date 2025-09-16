config.load_autoconfig(False)

# ============================================================================
# COLORS - Pure Black & White
# ============================================================================

# Completion menu
c.colors.completion.category.bg = '#000000'
c.colors.completion.category.fg = '#ffffff'
c.colors.completion.even.bg = '#000000'
c.colors.completion.fg = '#ffffff'
c.colors.completion.item.selected.bg = '#ffffff'
c.colors.completion.item.selected.fg = '#000000'
c.colors.completion.odd.bg = '#000000'

# Status bar
c.colors.statusbar.normal.bg = '#000000'
c.colors.statusbar.normal.fg = '#ffffff'
c.colors.statusbar.command.bg = '#000000'
c.colors.statusbar.command.fg = '#ffffff'
c.colors.statusbar.insert.bg = '#000000'
c.colors.statusbar.insert.fg = '#ffffff'
c.colors.statusbar.url.fg = '#ffffff'

# Tabs
c.colors.tabs.bar.bg = '#000000'
c.colors.tabs.even.bg = '#000000'
c.colors.tabs.even.fg = '#ffffff'
c.colors.tabs.odd.bg = '#000000'
c.colors.tabs.odd.fg = '#ffffff'
c.colors.tabs.selected.even.bg = '#ffffff'
c.colors.tabs.selected.even.fg = '#000000'
c.colors.tabs.selected.odd.bg = '#ffffff'
c.colors.tabs.selected.odd.fg = '#000000'

# Messages
c.colors.messages.error.bg = '#000000'
c.colors.messages.error.fg = '#ffffff'
c.colors.messages.info.bg = '#000000'
c.colors.messages.info.fg = '#ffffff'

# Hints
c.colors.hints.bg = '#000000'
c.colors.hints.fg = '#ffffff'

# Dark mode for web pages
c.colors.webpage.darkmode.enabled = True

# ============================================================================
# INTERFACE
# ============================================================================

# Hide tabs by default, show when switching for 2 seconds
c.tabs.show = 'switching'
c.tabs.show_switching_delay = 2000

# Hide status bar, show only in command/insert mode
c.statusbar.show = 'in-mode'

# Simple status bar widgets
c.statusbar.widgets = ['url', 'progress']

# Iosevka font
c.fonts.default_family = 'Iosevka, monospace'
c.fonts.default_size = '12pt'

# Hide scrollbars
c.scrolling.bar = 'never'

# ============================================================================
# PERFORMANCE & PRIVACY
# ============================================================================

# Faster browsing
c.content.autoplay = False
c.content.cookies.accept = 'no-3rdparty'
c.content.headers.do_not_track = True

# Memory optimization
c.content.cache.size = 50 * 1024 * 1024  # 50 MB
c.session.lazy_restore = True

# Extra Chromium flags for memory/performance
c.qt.args = [
    "disable-gpu-memory-buffer-compositor",
    "disable-background-timer-throttling",
    "disable-renderer-backgrounding",
    "disable-backgrounding-occluded-windows"
]

# Downloads
c.downloads.location.directory = '~/Downloads'
c.downloads.location.prompt = False

print("Optimized qutebrowser config loaded!")

