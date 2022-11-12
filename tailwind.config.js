/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "../templates/**/*.{html,js}",
        './apollo_blog/templates/base.html',
        './blog/templates/blog/*.html',
        './node_modules/flowbite/**/*.js',
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('flowbite/plugin')
    ]
}