import { computed, ref } from "vue";

import { MESSAGES } from "@/types/messages";
import axios from "axios";
import { defineStore } from "pinia";

export interface ITrainer {
  id: string | number;
  first_name: string;
  last_name: string;
  position: string;
  phone: string;
  email: string;
  bio: string;
  avatar: string;
  trainer_reviews: [];
  count_reviews?: number;
  total_rating?: number;
}

export const useCoachesStore = defineStore("coaches", () => {
  const trainers = ref<ITrainer[]>([]);
  const searchName = ref("");
  const selected = ref("");

  const getCoaches = async () => {
    try {
      const { data } = await axios.get("/api/workout/all-trainers/");
      trainers.value = data;
    } catch (err) {
      console.log("err", err);
      throw new Error(MESSAGES.COACHES_ERROR);
    }
  };

  const categories = ref([
    { value: "Инструктор бассейна", name: "Инструктор бассейна" },
    {
      value: "Инструктор тренажерного зала",
      name: "Инструктор тренажорного зала",
    },
    { value: "Инструктор йоги", name: "Тренер по йоге" },
  ]);

  const allCoaches = computed<ITrainer[]>(() => {
    if (selected.value && searchName.value) {
      return trainers.value
        .filter((coach) => coach.position === selected.value)
        .filter(
          (coach) =>
            coach.first_name
              .toLowerCase()
              .includes(searchName.value.toLowerCase()) ||
            coach.last_name
              .toLowerCase()
              .includes(searchName.value.toLowerCase())
        );
    } else if (selected.value) {
      return trainers.value.filter(
        (coach) => coach.position === selected.value
      );
    } else {
      if (searchName.value) {
        return trainers.value.filter(
          (coach) =>
            coach.first_name
              .toLowerCase()
              .includes(searchName.value.toLowerCase()) ||
            coach.last_name
              .toLowerCase()
              .includes(searchName.value.toLowerCase())
        );
      }
      return trainers.value;
    }
  });

  return { trainers, searchName, selected, categories, allCoaches, getCoaches };
});
