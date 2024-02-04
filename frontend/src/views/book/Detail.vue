<template>
    <Header></Header>

    DETAIL BOOK VIEW

    <BannerSuscription></BannerSuscription>
    <Footer></Footer>
</template>

<script setup>
    import Header from "@/components/layouts/Header.vue";
    import Footer from "@/components/layouts/Footer.vue";
    import BannerSuscription from "@/components/BannerSuscription.vue";
    import { onMounted, reactive, ref, watchEffect  } from "vue";
    import { useRoute } from "vue-router";
    import { useBookStore } from '@/stores/Book';

    const route = useRoute();
    const bookStore = useBookStore();
    const book_id = ref(0);
    const book = reactive({});

    onMounted(async () => await bookStore.fetchBooksData());

    watchEffect(async () => {
        book_id.value = parseInt(route.params.book_id);
        if (book_id.value) Object.assign(book, bookStore.bookById(book_id.value));
    });

</script>