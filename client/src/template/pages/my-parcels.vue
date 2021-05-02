<template>
  <div class='main'>
    <Transition name='fade'>
      <div v-if='infos_modal' class='fixed inset-0 w-full h-full flex items-center justify-center z-50'>
        <div class='modal-overlay absolute w-full h-full bg-gray-900 opacity-50'></div>
        <div class='block relative w-2/3 h-96 overflow-y-auto bg-white shadow-lg rounded-lg px-8 py-4'>
          <a aria-label='close'
             class='absolute top-0 right-0 text-xl text-gray-500 my-4 mx-4 outline-none hover:text-red-500 transition ease-in-out duration-150 cursor-pointer'
             @click.prevent="toggle('infos_modal')">
            <span class='icon-cancel-circle'></span>
          </a>
          <div class='flex flex-col justify-center items-center space-y-5'>
            <h2 class='text-2xl text-black font-extrabold'>{{ $t('information') }}</h2>
            <div class='flex flex-row justify-center items-center space-x-2 w-full'>
              <div class='flex flex-col justify-center space-y-2 w-1/2'>
                <h2 class='text-xl text-black font-extrabold text-center'>{{ $t('various') }}</h2>
                <div class='flex flex-row justify-center space-x-2'>
                  <span class='icon-crop'></span>
                  <label>
                    <input placeholder='H'
                           class='w-16 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                           type='text' disabled />
                  </label>
                  <p>x</p>
                  <label>
                    <input placeholder='L'
                           class='w-16 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                           type='text' disabled />
                  </label>
                  <p>x</p>
                  <label>
                    <input placeholder='P'
                           class='w-16 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                           type='text' disabled />
                  </label>
                  <p>{{ $t('in') }} cm</p>
                </div>
                <div class='flex flex-row justify-center items-center space-x-2'>
                  <span class='icon-download3'></span>
                  <label>
                    <input :placeholder="$t('parcel_weight')"
                           class='w-20 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                           type='text' disabled />
                  </label>
                  <p>{{ $t('in') }} kg</p>
                </div>
                <label class='flex flex-row justify-center items-center space-x-2'>
                  <span class='icon-spinner4'></span>
                  <p>{{ $t('packaging') }}</p>
                  <select class='w-32 border bg-white rounded px-3 py-2 outline-none'>
                    <option class='py-1' selected disabled>{{ $t('carton') }}</option>
                  </select>
                </label>
                <div class='flex flex-row justify-center items-center space-x-2'>
                  <label>
                    <input type='checkbox' checked disabled />
                    Type
                  </label>
                  <div class=''>
                    <label>
                      <select class='w-full border bg-white rounded px-3 py-2 outline-none w-full'>
                        <option class='py-1' selected disabled>Documents</option>
                      </select>
                    </label>
                  </div>
                </div>
                <div class='flex flex-row justify-center items-center space-x-2'>
                  <label>
                    <input type='checkbox' checked disabled />
                    {{ $t('assured') }}
                  </label>
                  <div class=''>
                    <label>
                      <select class='w-full border bg-white rounded px-3 py-2 outline-none w-full'>
                        <option class='py-1' selected disabled>$15 - {{ $t('insurance') }} 2</option>
                      </select>
                    </label>
                  </div>
                </div>
                <label class='flex flex-row justify-center items-center space-x-2'>
                  <input type='checkbox' checked disabled />
                  <p>{{ $t('fragile') }}</p>
                </label>
              </div>
              <div class='flex flex-col justify-center space-y-2 w-1/2 text-center'>
                <h2 class='text-xl text-black font-extrabold'>{{ $t('parcel_tracking') }}</h2>
                <div class='flex flex-row justify-center items-center'>
                  <p class='text-sm text-left mr-6'>08:50</p>
                  <div class='flex flex-col justify-start border-l-2 border-red-500 text-left pl-6'>
                    <p>{{  $t('arrival_scan') }}</p>
                    <span class='uppercase'>REIMS, MARNE FR</span>
                  </div>
                </div>
                <div class='flex flex-row justify-center items-center'>
                  <p class='text-sm text-left mr-6'>08:50</p>
                  <div class='flex flex-col justify-start border-l-2 border-red-500 text-left pl-6'>
                    <p>{{  $t('arrival_scan') }}</p>
                    <span class='uppercase'>REIMS, MARNE FR</span>
                  </div>
                </div>
                <div class='flex flex-row justify-center items-center'>
                  <p class='text-sm text-left mr-6'>08:50</p>
                  <div class='flex flex-col justify-start border-l-2 border-red-500 text-left pl-6'>
                    <p>{{  $t('arrival_scan') }}</p>
                    <span class='uppercase'>REIMS, MARNE FR</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Transition>
    <div class='w-full flex items-start justify-between flex-row p-4'>
      <div class='p-6 rounded-lg shadow-lg overflow-hidden w-full'>
        <table class='table-auto border-transparent w-full'>
          <thead>
          <tr>
            <th class='w-2/12'>ID {{  $t('parcel') }}</th>
            <th class='w-4/12'><span class='icon-compass text-base'></span> {{  $t('current_position') }}</th>
            <th class='w-4/12'><span class='icon-home text-base'></span> {{  $t('destination') }}</th>
            <th class='w-1/12'>Status</th>
            <th class='w-2/12'>{{  $t('action') }}</th>
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
                <span class='icon-notification cursor-pointer hover:text-red-500 transition ease-in-out duration-150'
                      @click="toggle('infos_modal')"></span>
                <span class='icon-pencil cursor-pointer hover:text-red-500 transition ease-in-out duration-150'></span>
                <span class='icon-bin cursor-pointer hover:text-red-500 transition ease-in-out duration-150'></span>
              </section>
            </td>
          </tr>
          <tr class='text-center bg-gray-200'>
            <td>#12523154efezf</td>
            <td>Châlons-en-Champagne</td>
            <td>Reims</td>
            <td><span class='icon-truck text-yellow-600'></span></td>
            <td>
              <section>
                <span class='icon-notification cursor-pointer hover:text-red-500 transition ease-in-out duration-150'
                      @click="toggle('infos_modal')"></span>
                <span class='icon-pencil cursor-pointer hover:text-red-500 transition ease-in-out duration-150'></span>
                <span class='icon-bin cursor-pointer hover:text-red-500 transition ease-in-out duration-150'></span>
              </section>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue'

export default Vue.extend({
  layout: 'master',
  middleware: 'auth',
  data() {
    return {
      infos_modal: false
    }
  },
  methods: {
    toggle: function(modalName: string) {
      if (modalName === 'infos_modal') {
        this.infos_modal = !this.infos_modal
      }
    }
  }
})
</script>

<style lang='scss' scoped></style>