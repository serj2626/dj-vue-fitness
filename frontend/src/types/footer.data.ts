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
    icon: "fa-brands fa-telegram fa-xl",
    style: "color: #74c0fc",
  },
  {
    title: "Instagram",
    link: "#",
    icon: "fa-brands fa-instagram fa-xl",
    style: "color: #ffd43b",
  },
  {
    title: "Linkedin",
    link: "#",
    icon: "fa-brands fa-linkedin fa-xl",
    style: "color: #74c0fc",
  },
  {
    title: "VK",
    link: "#",
    icon: "fa-brands fa-vk fa-xl",
    style: "color: #74c0fc",
  },
  {
    title: "GitHub",
    link: "#",
    icon: "fa-brands fa-github fa-xl",
    style: "color: white",
  },
];
