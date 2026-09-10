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
			title: '/home/hardware',

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
                        "articles/alimentations-et-vrm/alims",
                        "articles/refroidissement-airflow-et-tdp/airflow",
                        "articles/le-gros-son-de-nos-pc/audio",
                        "articles/cartes-meres/motherboard",
                        "articles/processeurs/cpu",
                        "articles/de-texte-a-processeur/rtl",
                        "articles/un-i5-est-un-i9-rate/binning",
                        "articles/overclocking-et-au-dela/overclocking",
                        "articles/stockage-et-bits/stockage",
                        "articles/ne-perdons-pas-la-memoire/memory",
                        "articles/entre-vitesse-et-stabilite/xmp",
                        "articles/explorons-nos-gpu/gpu",
                        "articles/les-os/os",
                        "articles/pilotes-et-materiel/drivers",
                        "articles/internet-et-ips/internet",
                        "articles/le-bottleneck/bottleneck",
                        "articles/quand-vos-pixels-vous-mentent/screen",
                        "articles/normes-et-magouilles/normes",  
                    ]
                },
                {
                    label: 'Tutos',
                    items: [
                        "tutorials/attention-a-la-douane/douanes",
                        "tutorials/conversion-mbr-gpt/convert",
                        "tutorials/csm/csm",
                        "tutorials/drivers/drivers",
                        "tutorials/emplacement-par-defaut/emplacement",
                        "tutorials/enceintes-qui-buzz/buzz",
                        "tutorials/casques-micro-gaming/mics",
                        "tutorials/bien-placer-son-micro/mics",
                        "tutorials/formatter/format",
                        "tutorials/partitions/partitions",
                        "tutorials/pas-de-connexion-internet-pendant-l-installation/connexion",
                        "tutorials/pilote-de-media-manquant/media",
                        "tutorials/prendre-de-belles-photos/photos"
                    ]
                },
                {
                    label: 'Tips',
                    items: []
                },
                {
                    label: 'Communauté',
                    items: [
                        "commu/controler-ses-ventilateurs/fans",
                        "commu/fe-ou-custom/gpu",
                        "commu/garanties-menteuses/garantie",
                        "commu/le-minage-est-il-mauvais/minage",
                        "commu/qu-est-ce-que-c-est-un-os/os",
                        "commu/c-est-quoi-la-hifi/hifi",
                    ]
                }
			],
		}),
	],
});
