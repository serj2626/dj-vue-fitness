export interface IAbonement {
  id: number;
  title: string;
  description: string;
  price: number;
  number_of_months: number;
}

export interface ICreateOrderAbonement {
  abonement: IAbonement;
  start: Date;
}

export interface IMyAbonement {
  abonement: IAbonement;
  id: number;
  start: Date;
  end: Date;
  status: boolean;
  active: boolean;
}
