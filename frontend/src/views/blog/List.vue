<template>
    <Header></Header>

    LIST BLOG VIEW

    <BannerSuscription></BannerSuscription>
    <Footer></Footer>
</template>

<script setup>
    import Header from "@/components/layouts/Header.vue";
    import Footer from "@/components/layouts/Footer.vue";
    import BannerSuscription from "@/components/BannerSuscription.vue";
    import { ref, onMounted,  } from 'vue';
    import { useBlogStore } from '@/stores/blog';

    const blogStore = useBlogStore();
    const blogs = ref([]);

    onMounted(async () => blogStore.fetchBlogs());

</script>