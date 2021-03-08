<template>
  <div class='main'>
    <div class='w-full flex items-start justify-between flex-row p-4'>
      <div class='p-6 rounded-lg shadow-lg overflow-hidden w-2/3'>
        <table class='table-auto border-transparent w-full'>
          <thead>
          <tr>
            <th class='w-2/12'>ID Colis</th>
            <th class='w-4/12'><span class='icon-compass text-base'></span> Position actuelle</th>
            <th class='w-4/12'><span class='icon-home text-base'></span> Destination</th>
            <th class='w-1/12'>Status</th>
            <th class='w-2/12'>Actions</th>
          </tr>
          </thead>
          <tbody>
          <tr class='text-center bg-gray-200'>
            <td>#12523154efezf</td>
            <td>Châlons-en-Champagne</td>
            <td>Reims</td>
            <td><span class='icon-truck text-yellow-600'></span></td>
            <td>
              <section>
                <span class='icon-notification'></span>
                <span class='icon-pencil'></span>
                <span class='icon-bin'></span>
              </section>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
      <div class='w-1/3 px-6'>
        <div class='flex flex-col rounded-lg shadow-lg overflow-hidden'>
          <div class='flex-1 bg-white p-6 flex flex-col justify-between'>
            <div class='flex-1'>
              <p class='text-sm leading-5 font-medium text-red-500 uppercase'>Vous êtes fournisseur ?</p>
              <div class='block'>
                <p class='mt-2 text-sm font-semibold text-gray-900'>Vous pouvez déposez des colis afin de les
                  transporter à tout va.</p>
              </div>
            </div>
            <div class='mt-6 flex items-center'>
              <a href='https://www.adobe.com/fr/products/indesign.html'
                 class='py-2 px-3 rounded-full text-white bg-red-500 hover:bg-red-400'>Déposer un colis</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue'

export default Vue.extend({
  layout: 'master'
})
</script>

<style lang='scss' src='./index.scss'></style>