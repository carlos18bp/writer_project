<template>
    <Header></Header>

    LIST BOOK VIEW

    <BannerSuscription></BannerSuscription>
    <Footer></Footer>
</template>

<script setup>
    import Header from "@/components/layouts/Header.vue";
    import Footer from "@/components/layouts/Footer.vue";
    import BannerSuscription from "@/components/BannerSuscription.vue";
    import { ref, onMounted,  } from 'vue';
    import { useBookStore } from '@/stores/blog';

    const bookStore = useBookStore();
    const books = ref([]);

    onMounted(async () => bookStore.fetchBooks());

</script>