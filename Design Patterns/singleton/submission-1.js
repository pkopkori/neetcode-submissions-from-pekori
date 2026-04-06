class Singleton {
    static instance;
    #value = null;

    /**
     * In JavaScript consider this method as the 'getInstance'
     */
    constructor() {
        if (Singleton.instance) {
            return Singleton.instance
        }
        Singleton.instance = this;
    }

    /**
     * @return {string}
     */
    getValue() {
        return this.#value;
    }

    /**
     * @param {string} value
     * @return {void}
     */
    setValue(value) {
        this.#value = value
    }
}
