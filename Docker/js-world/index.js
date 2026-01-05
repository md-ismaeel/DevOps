export const debounce = async (fn, delay) => {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => fn(...args), delay);
    };
};


export const arr = ["Apple", "Banana", "Orange", "Pineapple", "Watermelon"];