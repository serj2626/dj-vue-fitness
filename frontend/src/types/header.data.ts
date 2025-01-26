export interface IHeaderLink {
  title: string;
  link: string;
  class: string;
}

export const headerLinks: IHeaderLink[] = [
  {
    title: "О клубе",
    link: "#about",
    class: "header__link",
  },
  {
    title: "Абонементы",
    link: "#abonements",
    class: "header__link",
  },
  {
    title: "Тренеры",
    link: "#coaches",
    class: "header__link",
  },
  {
    title: "FAQ",
    link: "#faq",
    class: "header__link",
  },
  {
    title: "Контакты",
    link: "#contacts",
    class: "header__link",
  },
];
