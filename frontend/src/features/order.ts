import axios from "axios";

const $GetMyAbonementsList = async () => {
  const { data } = await axios.get("/api/auth/my-abonements/");
  return data;
};

const $DelAbonement = async (id: string) => {
  await axios.delete(`/api/auth/my-abonements/${id}/delete`);
};

const $DelTraining = async (id: string) => {
  await axios.delete(`/api/auth/my-trainings/${id}/delete`);
};

const $GetMyTrainingsList = async () => {
  const { data } = await axios.get("/api/auth/my-trainings/");
  return data;
};

export {
  $DelAbonement,
  $GetMyAbonementsList,
  $DelTraining,
  $GetMyTrainingsList,
};
