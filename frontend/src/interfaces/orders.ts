import type { IUserData } from "./auth";
import type { iRate, ITrainer } from "./workout";

export interface IAbonement {
  id: number;
  title: string;
  description: string;
  price: number;
  number_of_months: number;
  start?: Date;
  end?: Date;
  status?: boolean;
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

export interface IMyTrainig {
  id?: number | string;
  start: Date;
  end: Date;
  status: boolean;
  active: boolean;
  rate: iRate;
  trainer: ITrainer;
  user?: IUserData | null;
}
