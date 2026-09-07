// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://astro.build/config
export default defineConfig({

    site: 'https://https://home-hardware.app/',
    // base: '/home-hardware',

    markdown: {
        remarkPlugins: [remarkMath],
        rehypePlugins: [rehypeKatex],
    },

	integrations: [
		starlight({
			title: 'home-hardware',

            defaultLocale: 'root',
            locales: {
                root: {
                    label: 'Français',
                    lang: 'fr',
                },
            },

            
			social: [
                { icon: 'github', label: 'GitHub', href: 'https://github.com/lheywang/home-hardware' }, 
                {icon: 'discord', label: 'Discord', href: 'https://discord.gg/R9HNVnBs6s'}
            ],

            customCss: [
                './src/styles/custom.css',
                'katex/dist/katex.min.css'
            ],

			sidebar: [
				{
					label: 'Articles',
                    items: [
                        { label: "Vue d'ensemble", link: '/articles' },
                        { autogenerate: { "directory": "articles" } },]
				},
                {
                    label: 'Tutos',
                    items: [
                        { label: "Vue d'ensemble", link: '/tutorials' },
                        { autogenerate: { "directory": "tutorials" } }
                    ]
                },
                {
                    label: 'Tips',
                    items: [
                        { label: "Vue d'ensemble", link: '/tips' },
                        { autogenerate: { "directory": "tips" } }
                    ]
                },
                {
                    label: 'Communauté',
                    items: [
                        { label: "Vue d'ensemble", link: '/commu' },
                        { autogenerate: { "directory": "commu" } }
                    ]
                }
			],
		}),
	],
});
