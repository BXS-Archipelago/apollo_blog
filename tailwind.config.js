/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './apollo_blog/templates/**/*.html',
        './blog/templates/**/*.html',
        './node_modules/flowbite/**/*.js',
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('flowbite/plugin')
    ]
}