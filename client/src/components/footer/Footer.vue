<template>
  <footer class='w-full block mt-3 h-auto mb-24 md:mb-6 py-12 md:py-6 px-3'>
    <div class='flex flex-col justify-center items-center space-y-2'>
      <div class='flex-row space-x-3 lg:space-x-20'>
        <a href='' class='text-base text-lg hover:text-red-500 transition ease-in-out duration-150'>{{ $t('home_nav_title') }}</a>
        <a href='/prices' class='text-base text-lg hover:text-red-500 transition ease-in-out duration-150'>{{ $t('tariff_nav_title') }}</a>
        <a href='/my-parcels' class='text-base text-lg hover:text-red-500 transition ease-in-out duration-150'>{{ $t('parcels_nav_title') }}</a>
        <a href='/authentication' class='text-base text-lg hover:text-red-500 transition ease-in-out duration-150'>{{ $t('login_nav_title') }}</a>
      </div>
      <div class='text-base text-lg text-center'>
        <p>Copyright © <span class='font-extrabold text-red-500'>RT'Ransport</span> 2021. {{ $t('copyright')}}</p>
      </div>
    </div>

  </footer>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style lang='scss' src='./Footer.scss'></style>
