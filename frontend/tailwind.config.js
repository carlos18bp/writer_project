/** @type {import('tailwindcss').Config} */
export default {
    content: [
      "./index.html",
      "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
      extend: {
        letterSpacing: {
          tighter: '-.075em',
          tight: '-.05em',
          normal: '0',
          wide: '.025em',
          wider: '.05em',
          widest: '.25em'
        },
        colors: {

        },
        fontFamily: {

        },
      },
    },
    plugins: [
      require('@tailwindcss/aspect-ratio'),
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),
    ],
  }