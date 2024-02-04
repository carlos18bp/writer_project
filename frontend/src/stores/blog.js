import { defineStore } from "pinia";
import { get_request } from "./services/request_http";

export const useBlogStore = defineStore("blog", {
  state: () => ({
    blogs: [],
    areUpdateBlogs: false,
  }),
  getters: {
    /**
     * Get blog by id.
     * @param {object} state - State. 
     * @returns {array} - blog by id occurrence.
     */
    blogById: (state) => (blogId) => {
      return state.blogs.find(blog => blog.id === blogId);
    },
  },
  actions: { 
    /**
     * Fetch data from backend.
     */
    async init() {
      if(!this.areUpdateBlogs) this.fetchBlogsData();
    },
    /**
     * Fetch blogs from backend.
     */
    async fetchBlogsData() {
      if(this.areUpdateBlogs) return;

      let jsonData = await get_request('blogs/');

      if (jsonData && typeof jsonData === 'string') {
        try {
          jsonData = JSON.parse(jsonData)
        } catch (error) {
          console.error(error.message);
          jsonData = [];
        }
      }
      
      this.blogs = jsonData ?? [];
      console.log('Source: blogs, count: '+ this.blogs.length);
      console.log(this.blogs);
      
      this.areUpdateBlogs = true;
    },
  }
});