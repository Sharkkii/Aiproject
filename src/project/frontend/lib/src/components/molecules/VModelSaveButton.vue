<template>
<div id="v-model-save-button">
  <form method="POST" v-on:submit.prevent="submit">
    <div class="items">
      <div class="item">
        <button type="submit" v-bind:disabled="disabled">
          <p>Save Model</p>
        </button>
      </div>
    </div>
  </form>
</div>
</template>

<style scoped lang="scss">
.items {
  display: flex;
  align-items: flex-end;
  height: 100px;
}

.item {

  width: 100%;

  input {
    box-sizing: border-box;
    font-size: 20px;
    height: 50px;
    width: 100%;
  }

  button {
    box-sizing: border-box;
    font-size: 20px;
    height: 50px;
    width: 100%;
  }
}
</style>

<script>
export default {
  name: "VModelSaveButton",
  data: function() {
    return {
      name: "",
      disabled: true
    }
  },
  props: {
    status: {
      type: String,
      default: "NG"
    }
  },
  methods: {
    saveModel: function(data) {
      this.$emit("save-model", data);
    },
    submit: function() {
      this.saveModel({
        name: this.name
      })
    }
  },
  watch: {
    status: function() {
      if (this.status == "OK") {
        this.disabled = false
      } else if (this.status == "NG") {
        this.disabled = true
      }
    }
  }
}
</script>
