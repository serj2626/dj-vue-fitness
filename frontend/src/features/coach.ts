import axios from "axios";

const $GetCoach = async (id: string & { __uuid: true }) => {
  const { data } = await axios.get(`/api/workout/trainers/${id}`);
  return data;
};

const $GetCoachList = async () => {
  const { data } = await axios.get("/api/workout/all-trainers/");
  return data;
};

export { $GetCoach, $GetCoachList };
