import { defineStore } from "pinia";
import { get_request } from "./services/request_http";

export const useBookStore = defineStore("Book", {
  state: () => ({
    books: [],
    areUpdateBooks: false,
  }),
  getters: {
    /**
     * Get Book by id.
     * @param {object} state - State. 
     * @returns {array} - Book by id occurrence.
     */
    bookById: (state) => (bookId) => {
      return state.books.find(book => book.id === bookId);
    },
  },
  actions: { 
    /**
     * Fetch data from backend.
     */
    async init() {
      if(!this.areUpdateBooks) this.fetchBooksData();
    },
    /**
     * Fetch Books from backend.
     */
    async fetchBooksData() {
      if(this.areUpdateBooks) return;

      let jsonData = await get_request('books/');

      if (jsonData && typeof jsonData === 'string') {
        try {
          jsonData = JSON.parse(jsonData)
        } catch (error) {
          console.error(error.message);
          jsonData = [];
        }
      }
      
      this.books = jsonData ?? [];
      console.log('Source: books, count: '+ this.books.length);
      console.log(this.books);
      
      this.areUpdateBooks = true;
    },
  }
});