<template>
<div id="v-task-create-button">
  <form method="POST" v-on:submit.prevent="submit">
    <div class="item">
      <label>
        <p>Task Name</p>
        <div><input type="text" v-model="taskName"></div>
      </label>
    </div>
    <div class="item">
      <label>
        <p>Required Effort</p>
        <div><input type="number" v-model="requiredEffort"></div>
      </label>
    </div>
    <div class="item">
      <label>
        <p>Due</p>
        <div><input type="date" v-model="due"></div>
      </label>
    </div>
    <div class="item">
      <button type="submit">
        <p>Create</p>
      </button>
    </div>
  </form>
</div>
</template>

<style scoped lang="scss">
.item {
  margin-top: 10px;

  input {
    font-size: 20px;
    height: 50px;
    width: 100%;
  }

  button {
    font-size: 20px;
    height: 50px;
    width: 100%;
  }
}
</style>

<script>
export default {
  name: "VTaskCreateButton",
  data: function() {
    return {
      taskName: null,
      requiredEffort: null,
      due: null
    }
  },
  methods: {
    createTask: function(data) {
      this.$emit("create-task", data)
    },
    submit: function() {
      this.createTask({
        task_name: this.taskName,
        due: this.due,
        required_effort: this.requiredEffort
      })
    }
  }
}
</script>