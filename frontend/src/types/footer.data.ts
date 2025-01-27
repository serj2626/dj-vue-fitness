import { Icons } from "./icons";

interface IFooterLink {
  title: string;
  link: string;
  icon: string;
  style?: string;
}

export const footerLinks: IFooterLink[] = [
  {
    title: "Telegram",
    link: "#",
    icon: Icons.TG,
    style: "color: #74c0fc",
  },
  {
    title: "Instagram",
    link: "#",
    icon: Icons.Insta,
    style: "color: #cc5a29",
  },
  {
    title: "Linkedin",
    link: "#",
    icon: Icons.Linkedin,
    style: "color: #74c0fc",
  },
  {
    title: "VK",
    link: "#",
    icon: Icons.VK,
    style: "color: #74c0fc",
  },
  {
    title: "GitHub",
    link: "#",
    icon: Icons.Github,
    style: "color: white",
  },
];
