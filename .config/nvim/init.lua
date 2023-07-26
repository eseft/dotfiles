local g   = vim.g
local o   = vim.opt
local api = vim.api
-- Set options
o.mouse          = 'a'                               -- Mouse support
o.clipboard      = 'unnamedplus'                     -- Copy/Paste to system clipboard
o.swapfile       = false                             -- Don't use swapfile
o.completeopt    = 'menuone,noinsert,noselect'       -- Autocomplete options
o.number         = true
o.relativenumber = true
o.smartindent    = true
o.shiftwidth     = 4
o.tabstop        = 4
o.list           = true
o.listchars      = 'eol:$,tab:<->,extends:>,precedes:<,lead:.,space:-,multispace:---+'


-- Automatically install packer
local fn = vim.fn
local install_path = fn.stdpath('data') .. '/site/pack/packer/start/packer.nvim'

if fn.empty(fn.glob(install_path)) > 0 then
  packer_bootstrap = fn.system({
    'git',
    'clone',
    '--depth',
    '1',
    'https://github.com/wbthomason/packer.nvim',
    install_path
  })
  vim.o.runtimepath = vim.fn.stdpath('data') .. '/site/pack/*/start/*,' .. vim.o.runtimepath
end

-- Autocommand that reloads neovim whenever you save the init.lua file
vim.cmd [[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost init.lua source <afile> | PackerSync
  augroup end
]]

-- Use a protected call so we don't error out on first use
local status_ok, packer = pcall(require, 'packer')
if not status_ok then
  return
end

-- Install plugins
require("packer").startup(
  function()
    -- Add you plugins here:
    use 'wbthomason/packer.nvim' -- packer can manage itself

    -- Lua line
    use 'nvim-lualine/lualine.nvim'

    -- Dev icons
    use 'kyazdani42/nvim-web-devicons'

    -- Nerdtree
    use 'preservim/nerdtree'

    -- Dracula
    use 'Mofiqul/dracula.nvim'

    -- Lsp config
    use 'neovim/nvim-lspconfig'

    -- Go plugin
    use 'fatih/vim-go'
  end
)

api.nvim_command [[colorscheme dracula]]
api.nvim_set_keymap("n", "<C-t>", ":NERDTreeToggle<CR>", {noremap = true})

-- Set some of my mappings
-- Quick jumps between buffers
api.nvim_set_keymap("n", "]b", ":bnext<CR>", {noremap = true})
api.nvim_set_keymap("n", "[b", ":bprevious<CR>", {noremap = true})
-- Go plugin bindings
api.nvim_set_keymap("n", "<space>gr", ":GoRun<CR>", {noremap = true})

require('lualine').setup{
  options = {
    icons_enabled = true,
    theme = 'dracula-nvim',
    component_separators = { left = '', right = ''},
    section_separators = { left = '', right = ''},
    disabled_filetypes = {},
    always_divide_middle = true,
    globalstatus = false,
  },
  sections = {
    lualine_a = {'mode'},
    lualine_b = {'branch', 'diff', 'diagnostics'},
    lualine_c = {'filename'},
    lualine_x = {'encoding', 'fileformat', 'filetype'},
    lualine_y = {'progress'},
    lualine_z = {'location'}
  },
  inactive_sections = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {'filename'},
    lualine_x = {'location'},
    lualine_y = {},
    lualine_z = {}
  },
  tabline = {},
  extensions = {}
}
-- Mappings.
local opts = { noremap=true, silent=true }
-- See `:help vim.diagnostic.*` for documentation on any of the below functions
vim.keymap.set('n', '<space>e', vim.diagnostic.open_float, opts)
vim.keymap.set('n', '[d', vim.diagnostic.goto_prev, opts)
vim.keymap.set('n', ']d', vim.diagnostic.goto_next, opts)
vim.keymap.set('n', '<space>q', vim.diagnostic.setloclist, opts)

-- Use an on_attach function to only map the following keys
-- after the language server attaches to the current buffer
local on_attach = function(client, bufnr)
  -- Enable completion triggered by <c-x><c-o>
  api.nvim_buf_set_option(bufnr, 'omnifunc', 'v:lua.vim.lsp.omnifunc')

  -- Mappings.
  -- See `:help vim.lsp.*` for documentation on any of the below functions
  local bufopts = { noremap=true, silent=true, buffer=bufnr }
  vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, bufopts)
  vim.keymap.set('n', 'gd', vim.lsp.buf.definition, bufopts)
  vim.keymap.set('n', 'K', vim.lsp.buf.hover, bufopts)
  vim.keymap.set('n', 'gi', vim.lsp.buf.implementation, bufopts)
  vim.keymap.set('n', '<C-k>', vim.lsp.buf.signature_help, bufopts)
  vim.keymap.set('n', '<space>wa', vim.lsp.buf.add_workspace_folder, bufopts)
  vim.keymap.set('n', '<space>wr', vim.lsp.buf.remove_workspace_folder, bufopts)
  vim.keymap.set('n', '<space>wl', function()
    print(vim.inspect(vim.lsp.buf.list_workspace_folders()))
  end, bufopts)
  vim.keymap.set('n', '<space>D', vim.lsp.buf.type_definition, bufopts)
  vim.keymap.set('n', '<space>rn', vim.lsp.buf.rename, bufopts)
  vim.keymap.set('n', '<space>ca', vim.lsp.buf.code_action, bufopts)
  vim.keymap.set('n', 'gr', vim.lsp.buf.references, bufopts)
  vim.keymap.set('n', '<space>f', vim.lsp.buf.formatting, bufopts)
end

local lsp_flags = {
	-- This is the default in Nvim 0.7+
	debounce_text_changes = 150,
}
require('lspconfig')['pylsp'].setup{
	on_attach = on_attach,
	flags = lsp_flags,
}
require('lspconfig')['gopls'].setup{
	on_attach = on_attach,
	flags = lsp_flags,
}
require('lspconfig')['clangd'].setup{
	on_attach = on_attach,
	flags = lsp_flags,
	filetypes = {"c", "cpp"},
}
-- require('lspconfig')['omnisharp'].setup{
-- 	on_attach = on_attach,
-- 	flags = lsp_flags,
-- 	filetypes = {"cs"},
-- }
