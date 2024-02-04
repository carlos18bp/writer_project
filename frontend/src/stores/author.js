import { defineStore } from "pinia";
import { get_request } from "./services/request_http";

export const useAuthorStore = defineStore("Author", {
  state: () => ({
    author: {},
    areUpdateAuthor: false,
  }),
  actions: { 
    /**
     * Fetch data from backend.
     */
    async init() {
      if(!this.areUpdateAuthor) this.fetchAuthorData();
    },
    /**
     * Fetch Authors from backend.
     */
    async fetchAuthorData() {
      if(this.areUpdateAuthor) return;

      let jsonData = await get_request('author/');

      if (jsonData && typeof jsonData === 'string') {
        try {
          jsonData = JSON.parse(jsonData)
        } catch (error) {
          console.error(error.message);
          jsonData = [];
        }
      }
      
      this.author = jsonData ?? [];
      console.log('Source: Author, count: '+ this.author.length);
      console.log(this.author);
      
      this.areUpdateAuthor = true;
    },
  }
});