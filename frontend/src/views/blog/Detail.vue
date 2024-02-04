<template>
    <Header></Header>

    DETAIL BLOG VIEW

    <BannerSuscription></BannerSuscription>
    <Footer></Footer>
</template>

<script setup>
    import Header from "@/components/layouts/Header.vue";
    import Footer from "@/components/layouts/Footer.vue";
    import BannerSuscription from "@/components/BannerSuscription.vue";
    import { onMounted, reactive, ref, watchEffect  } from "vue";
    import { useRoute } from "vue-router";
    import { useBlogStore } from '@/stores/blog';

    const route = useRoute();
    const blogStore = useBlogStore();
    const blog_id = ref(0);
    const blog = reactive({});

    onMounted(async () => await blogStore.fetchBlogsData());

    watchEffect(async () => {
        blog_id.value = parseInt(route.params.blog_id);
        if (blog_id.value) Object.assign(blog, blogStore.blogById(blog_id.value));
    });

</script>