<template>
    <Header></Header>

    BIOGRAPHIC VIEW

    <BannerSuscription></BannerSuscription>
    <Footer></Footer>
</template>

<script setup>
    import Header from "@/components/layouts/Header.vue";
    import Footer from "@/components/layouts/Footer.vue";
    import BannerSuscription from "@/components/BannerSuscription.vue";
    import { reactive, onMounted,  } from 'vue';
    import { useAuthorStore } from '@/stores/blog';

    const authorStore = useAuthorStore();
    const author = reactive({});

    onMounted(async () => authorStore.fetchAuthor());

</script>