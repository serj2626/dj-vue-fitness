import axios from "axios";

interface IFormReview {
  message: string;
  rating: number | null;
}

const $CreateReview = async (form: IFormReview, coachId: string & { __uuid: true }) => {
  const res = await axios.post("/api/workout/reviews/create", {
    text: form.message,
    trainer: coachId,
    rating: form.rating,
  });
  return res;
};
const $DelReview = async (id: number) => {
  await axios.delete(`/api/workout/reviews/${id}`);
};

export { $CreateReview, $DelReview };
