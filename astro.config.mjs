// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({

    site: 'https://lheywang.github.io',
    base: '/home-hardware',

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
            ],

			sidebar: [
				{
					label: 'Guides',
                    items: [{ autogenerate: { "directory": "articles" } }]
					
				},
			],
		}),
	],
});
