// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://astro.build/config
export default defineConfig({

    site: 'https://home-hardware.app/',
    // base: '/home-hardware',

    markdown: {
        remarkPlugins: [remarkMath],
        rehypePlugins: [rehypeKatex],
    },

	integrations: [
		starlight({
			title: '/home/hardware',

            components: {
                Head: './src/content/components/head.astro',
            },

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
                    collapsed: false,
                    items: [

                        {
                            label: "Alimentations",
                            collapsed: false,
                            items: [
                                { label: "Alimentations et VRMs",           slug: "articles/alimentations-et-vrm/alims"},
                                { label: "Tension et overclocking",         slug: "articles/overclocking-et-au-dela/overclocking"}
                            ]
                        },
                        {
                            label: "Visites",
                            collapsed: false,
                            items: [
                                { label: "Visite d'une carte mère",         slug: "articles/cartes-meres/motherboard"},
                                { label: "Visite d'une carte graphique",    slug: "articles/explorons-nos-gpu/gpu"}
                            ]
                        },
                        {
                            label: "Architecture & Processeurs",
                            collapsed: false,
                            items: [
                                { label: "Fonctionnement d'un CPU",         slug: "articles/processeurs/cpu"},
                                { label: "Conception d'un CPU",             slug: "articles/de-texte-a-processeur/rtl"},
                                { label: "Gammes et triages",               slug: "articles/un-i5-est-un-i9-rate/binning"},
                                { label: "Bottleneck et limitations",       slug: "articles/le-bottleneck/bottleneck"},
                                { label: "Mémoires et Caches",              slug: "articles/quand-votre-processeur-joue-a-cache-cache/caches"},
                                { label: "Physique et fréquence max",       slug: "articles/pourquoi-mon-processeur-est-limite-en-frequence-max/freq"}
                            ]
                        },
                        {
                            label: "Stockage & Mémoire",
                            collapsed: false,
                            items: [
                                { label: "Comment on stocke une donnée ?",  slug: "articles/stockage-et-bits/stockage"},
                                { label: "Et pendant que mon pc tourne ?",  slug: "articles/ne-perdons-pas-la-memoire/memory"},
                                { label: "L'XMP, booster gratuit !",        slug: "articles/entre-vitesse-et-stabilite/xmp"}
                            ]
                        },
                        {
                            label: "Refroidissement",
                            collapsed: false,
                            items: [
                                { label: "Théorie et airflow",              slug: "articles/refroidissement-airflow-et-tdp/airflow"}
                            ]
                        },
                        {
                            label: "Audio & Analogique",
                            collapsed: false,
                            items: [
                                { label: "Le gros son de nos PC",           slug: "articles/le-gros-son-de-nos-pc/audio"},
                            ]
                        },
                        {
                            label: "Systèmes d'exploitation",
                            collapsed: false,
                            items: [
                                { label: "Fonctionnement d'un OS",          slug: "articles/les-os/os"},
                                { label: "Et nos drivers ?",                slug: "articles/pilotes-et-materiel/drivers"}
                            ]
                        },
                        {
                            label: "Internet & Transferts de données",
                            collapsed: false,
                            items: [
                                { label: "Internet et IPs",                 slug: "articles/internet-et-ips/internet"}
                            ]
                        },
                        {
                            label: "Standards & Normes",
                            collapsed: false,
                            items: [
                                { label: "Normes et magouilles",            slug: "articles/normes-et-magouilles/normes"},
                                { label: "GPMI, le futur USB-C ?",          slug: "articles/usb-c-en-fin-de-vie/gpmi"},
                            ]
                        },
                        {
                            label: "Affichage & Ecrans",
                            collapsed: false,
                            items: [
                                { label: "Quand vos pixels vous mentent",   slug: "articles/quand-vos-pixels-vous-mentent/screen"}
                            ]
                        },
                        
                    ]
                },
                {
                    label: 'Tutos',
                    collapsed: false,
                    items: [
                        {
                            label: "Achats",
                            collapsed: false,
                            items: [
                                { label: "Attention à la douane",   slug: "tutorials/attention-a-la-douane/douanes"}
                            ]
                        },
                        {
                            label: "Résolutions (Windows)",
                            collapsed: false,
                            items: [
                                { label: "Conversion MBR / GPT",   slug: "tutorials/conversion-mbr-gpt/convert"},
                                { label: "Formatter un disque",   slug: "tutorials/formatter/format"},
                                { label: "Partitionner un disque",   slug: "tutorials/partitions/partitions"},
                                { label: "Installer ses drivers",   slug: "tutorials/drivers/drivers"},
                                { label: "Pilote de média manquant", slug: "tutorials/pilote-de-media-manquant/media"},
                                { label: "Connexion internet pendant l'installation", slug: "tutorials/pas-de-connexion-internet-pendant-l-installation/connexion"},
                                { label: "Emplacement de stockage par défaut", slug: "tutorials/emplacement-par-defaut/emplacement"}
                            ]
                        },
                        {
                            label: "Résolutions (BIOS)",
                            collapsed: false,
                            items: [
                                { label: "Activer le CSM", slug: "tutorials/csm/csm"},
                            ]
                        },
                        {
                            label: "Photo",
                            collapsed: false,
                            items: [
                                {label: "Prendre de belles photos", slug: "tutorials/prendre-de-belles-photos/photos"}
                            ]
                        },
                        {
                            label: "Audio",
                            collapsed: false,
                            items: [
                                {label: "Enceintes qui buzz", slug: "tutorials/enceintes-qui-buzz/buzz"},
                                {label: "Casques micro gaming", slug: "tutorials/casques-micro-gaming/mics"},
                                {label: "Bien placer son micro", slug: "tutorials/bien-placer-son-micro/mics"}
                            ]
                        }
                    ]
                },
                {
                    label: 'Tips',
                    collapsed: true,
                    items: []
                },
                {
                    label: 'Communauté',
                    collapsed: true,
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
