<template>
  <div class="about-dialog-container">
    <app-modal :open="open" :dismiss="dismiss">
      <div class="page">
        <h3>關於舉報系統</h3>
        <p>
          農地違章工廠舉報系統為協助民眾回報揭露農地違章工廠資訊，並非實際完成舉報。
        </p>

        <p>
          地球公民基金會將整理資料進行部分案件追蹤，完成舉報者可於「已舉報」案件查見。
        </p>

        <p>
          105.05.20 前的違章工廠我們將持續收集資訊，但本系統優先針對新增建與中高污染違章工廠進行舉報。
        </p>

        <p>
          本系統感謝 #g0v.tw 頻道內所有協助開發的朋友們。
        </p>
      </div>
    </app-modal>
  </div>
</template>

<script lang="ts">
import AppModal from '@/components/AppModal.vue'
import { createComponent } from '@vue/composition-api'

export default createComponent({
  name: 'AboutModal',
  components: {
    AppModal
  },
  props: {
    open: {
      type: Boolean,
      default: false
    },
    dismiss: {
      type: Function
    }
  }
})
</script>

<style lang="scss">
@import '@/styles/page';
@import '@/styles/variables';

.about-dialog-container .app-modal {
  top: 47px;
  max-height: calc(100% - 100px);
  margin: 0 7px;

  .page h3 {
    color: $primary-color;
  }
}
</style>
