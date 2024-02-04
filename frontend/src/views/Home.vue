<template>
    <Header></Header>

    HOME VIEW

    <AboutMe></AboutMe>
    <LastestBooksCarousel></LastestBooksCarousel>
    <Review></Review>
    <VideoYoutubeCarousel></VideoYoutubeCarousel>

    <BannerSuscription></BannerSuscription>
    <Footer></Footer>
</template>

<script setup>
    import Header from "@/components/layouts/Header.vue";
    import Footer from "@/components/layouts/Footer.vue";
    import AboutMe from "@/components/AboutMe.vue";
    import LastestBooksCarousel from "@/components/home/LastestBooksCarousel.vue";
    import Review from "@/components/home/Review.vue";
    import VideoYoutubeCarousel from "@/components/VideoYoutubeCarousel.vue";

    import BannerSuscription from "@/components/BannerSuscription.vue";

</script>