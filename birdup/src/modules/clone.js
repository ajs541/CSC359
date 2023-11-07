function clone( someObject ) {
    return JSON.parse(JSON.stringify( someObject ));
} // clone()

export default clone;