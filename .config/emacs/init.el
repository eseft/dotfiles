(setq user-emacs-directory "~/.config/emacs")
(org-babel-load-file
 (expand-file-name "config.org"
                   user-emacs-directory))
