let username_value = $state('')

export const global_username = {
     get value() {
          return username_value
     },

     set value(new_val) {
          username_value = new_val
     }
}