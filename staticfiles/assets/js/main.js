header_navigation_item = document.querySelectorAll(".header_navigation_item")

header_navigation_item.forEach((element) => {
    header_navigation_links_wrapper = document.querySelectorAll(".header_navigation_links_wrapper")
    header_navigation_item_span = document.querySelectorAll(".header_navigation_item span")
    element.addEventListener("mouseenter", () => {
        inner_el = element.lastElementChild
        inner_el_first = element.firstElementChild
        header_navigation_links_wrapper.forEach((el) => {
            el.style.maxHeight = 0
        })
        header_navigation_item_span.forEach(element => {
            element.classList.remove("active")
        });
        setTimeout(() => {
            inner_el.style.display = "flex"
            inner_el.style.maxHeight = inner_el.scrollHeight  + "px"
            inner_el_first.classList.add("active")
        }, 200)
    })

    element.addEventListener("mouseleave", () => {
        inner_el = element.lastElementChild
        inner_el_first = element.firstElementChild
        inner_el.style.maxHeight = "0px"
        header_navigation_item_span.forEach((el) => {
            el.classList.remove(`active`)
        })
    })
})


let header_burger = document.querySelector(".header_burger")

header_burger.addEventListener('click', () => {
    header_burger.classList.toggle("active")
    let header_navigation_list = document.querySelector(".header_navigation_list")

    if (header_navigation_list.getBoundingClientRect().height) {
        header_navigation_list.style.maxHeight = `0px`
    }
    else {
        header_navigation_list.style.display = "flex"
        header_navigation_list.style.maxHeight = header_navigation_list.scrollHeight + 600 + "px"
    }

    header_navigation_item.forEach((element) => {
        inner_el = element.lastElementChild
        let header_navigation_item_span = document.querySelectorAll(".header_navigation_item span")
        header_navigation_item_span.forEach(element => {
            element.classList.remove("active")
        });
        let header_navigation_links_wrapper = document.querySelectorAll(".header_navigation_links_wrapper")
        inner_el.style.maxHeight = `0px`
    });
})

let hero_action_item = document.querySelectorAll(".main-hero_action_item")
let hero_action_posts = document.querySelectorAll(".main-hero_action_posts")
hero_action_item.forEach((element) => {
    element.addEventListener("click", () => {

        hero_action_item.forEach(element => {
            element.classList.remove("active")
        });

        element.classList.add("active")

        list_class = element.className.replace('main-hero_action_item ', "").replace(" active", "")

        hero_action_posts.forEach((element)=>{
            element.style.display = "none"
        })

        let hero_action_post = document.querySelector(`.main-hero_action_posts.${list_class}`)
        hero_action_post.style.display = "flex"
    })
});