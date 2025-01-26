import { MESSAGES } from "@/types/messages";
import axios from "axios";
import { defineStore } from "pinia";
import { ref } from "vue";
export interface IPost {
  id: string;
  category: string;
}

export const usePostsStore = defineStore("posts", () => {
  const posts = ref<IPost[]>([]);

  const getPosts = async () => {
    try {
      const { data } = await axios.get("/api/workout/posts/");
      posts.value = data;
    } catch (err) {
      throw new Error(MESSAGES.POSTS_ERROR);
    }
  };

  return { posts, getPosts };
});
