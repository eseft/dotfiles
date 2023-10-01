# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "j", lazy.layout.next(), desc="Move window focus to next window"),
    Key([mod], "k", lazy.layout.previous(), desc="Move window focus to previous window"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow(), lazy.layout.increase_nmaster(), desc="Move window to the right"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    # Bar Toggle
    Key([mod, "shift"], "b", lazy.hide_show_bar(), desc="Toggle bar"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "o", lazy.layout.maximize(), desc="Maximize window"),
    Key([mod], "e", lazy.spawn("emacsclient -c --alternate-editor=emacs"), desc="Launch emacsclient"),
    Key([mod], "Return", lazy.spawn("alacritty -e fish"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">",
        dmenu_font="Ubuntu:weight=bold:size=10",
    ))),

    # Keyboard Layouts
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(
        border_focus="#c678dd",
        border_normal="#000000",
        border_width=1,
        single_margin=4,
        new_client_position="top",
        margin=4
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    rounded = False,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 3,
                    highlight_method = "line",
                    active = colors[7],
                    inactive = colors[2],
                    highlight_color = colors[1],
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.CurrentLayoutIcon(
                    scale=0.8,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.WindowName(
                    foreground = colors[6],
                    background = colors[0]
                ),
                # widget.TextBox(
                #     text = "",
                #     padding = 10,
                #     foreground = colors[3],
                #     background = colors[0],
                #     fontsize = 16,
                # ),
                # widget.GenPollText(
                #     func = kernel_version,
                #     update_interval = 0.5,
                #     max_chars = 20,
                #     padding = 5,
                #     foreground = colors[3],
                #     background = colors[0],
                # ),
                widget.TextBox(
                    text = "󰌌",
                    padding = 5,
                    foreground = colors[5],
                    background = colors[0],
                    fontsize = 16,
                ),
                widget.KeyboardLayout(
                    foreground = colors[5],
                    background = colors[0],
                    configured_keyboards = ["us", "ru"],
                    padding = 5,
                    # decorations=[
                    #     BorderDecoration(
                    #         colour = colors[8],
                    #         border_width = [0, 0, 2, 0],
                    #         padding_x = 5,
                    #         padding_y = None,
                    #     )
                    # ],
                ),
                widget.TextBox(
                    text = "󰸗",
                    padding = 5,
                    foreground = colors[6],
                    background = colors[0],
                    fontsize = 16,
                ),
                widget.Clock(
                    format="%d/%m/%y %H:%M",
                    foreground = colors[6],
                    background = colors[0],
                    mouse_callbacks={"Button1": lazy.spawn("gsimplecal")}
                ),
                widget.Systray(
                    foreground = colors[2],
                    background = colors[0]
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="steam"),
        Match(wm_class="unityhub"),
        Match(wm_class="Unity"),
    ],
    border_focus = colors[1],
    border_normal = colors[0],
)

# Various hooks
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.client_managed
def set_gsimplecal_position(c):
    if c.name == "gsimplecal":
        c.cmd_set_position_floating(1680, 30)

def kernel_version():
    return subprocess.check_output(["uname", "-r"]).rstrip().lstrip().str()

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
