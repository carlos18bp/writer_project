<template>
  <div class="bg-background_p">
    <RouterView/>
  </div>
</template>

<script setup>
  import { onMounted } from 'vue';
  import { RouterView } from "vue-router";
  import { useAuthorStore } from '@/stores/author';
  import { useBlogStore } from '@/stores/blog';
  import { useBookStore } from '@/stores/book';
  
  const authorStore = useAuthorStore();
  const blogStore = useBlogStore();
  const bookStore = useBookStore();

  onMounted(async () => {
    await authorStore.init();
    await blogStore.init();
    await bookStore.init();
  });
</script>
