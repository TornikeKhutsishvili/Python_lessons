/* ============  Get Current Year  ============ */

const currYear = document.querySelector(".current-year")
const dt = new Date
let year = dt.getFullYear()
currYear.append(year)

// ===============================================
