// BengalClimate Analytics Dashboard Controller

document.addEventListener("DOMContentLoaded", () => {
    // --- STATE MANAGEMENT ---
    let selectedDistrict = "";
    let selectedYear = null;
    let charts = {};
    let isDarkMode = true;

    // --- DOM ELEMENTS ---
    const districtSelect = document.getElementById("districtSelect");
    const yearSelect = document.getElementById("yearSelect");
    const searchInput = document.getElementById("eventSearch");
    const eventTypeFilter = document.getElementById("eventTypeFilter");
    const themeToggleBtn = document.getElementById("themeToggle");
    
    // Metrics
    const metricAvgRainfall = document.getElementById("metric-avg-rainfall");
    const metricAvgRainfallSub = document.getElementById("metric-avg-rainfall-sub");
    const metricTotalEvents = document.getElementById("metric-total-events");
    const metricTotalEventsSub = document.getElementById("metric-total-events-sub");
    const metricWettestDistrict = document.getElementById("metric-wettest-district");
    const metricWettestVal = document.getElementById("metric-wettest-val");
    const metricImpactedPlace = document.getElementById("metric-impacted-place");
    
    const eventsTableBody = document.getElementById("eventsTableBody");
    const tableInfoCount = document.getElementById("tableInfoCount");
    
    // --- INITIALIZE UI ---
    function init() {
        populateDropdowns();
        setupEventListeners();
        calculateStaticMetrics();
        updateDashboard();
    }

    // Populate dropdown lists dynamically
    function populateDropdowns() {
        // Unique Districts
        const districts = [...new Set(RAINFALL_DATA.map(d => d.District))].sort();
        districts.forEach(dist => {
            const option = document.createElement("option");
            option.value = dist;
            option.textContent = dist;
            districtSelect.appendChild(option);
        });
        // Select Kolkata as default
        districtSelect.value = "Kolkata";
        selectedDistrict = "Kolkata";

        // Unique Years
        const years = [...new Set(RAINFALL_DATA.map(d => d.Year))].sort((a, b) => b - a);
        years.forEach(yr => {
            const option = document.createElement("option");
            option.value = yr;
            option.textContent = yr;
            yearSelect.appendChild(option);
        });
        // Select latest year as default
        yearSelect.value = years[0];
        selectedYear = parseInt(years[0]);
    }

    // --- METRIC CALCULATIONS ---
    function calculateStaticMetrics() {
        // Find most impacted place across all event records
        const placeCounts = {};
        EVENTS_DATA.forEach(ev => {
            const place = ev.Place.split(",")[0].trim();
            if (place) {
                placeCounts[place] = (placeCounts[place] || 0) + 1;
            }
        });
        let topPlace = "None";
        let topCount = 0;
        for (const [place, count] of Object.entries(placeCounts)) {
            if (count > topCount) {
                topCount = count;
                topPlace = place;
            }
        }
        metricImpactedPlace.textContent = topPlace;
    }

    function updateDynamicMetrics() {
        // 1. Avg rainfall for selected district
        const distData = RAINFALL_DATA.filter(d => d.District === selectedDistrict);
        if (distData.length > 0) {
            const total = distData.reduce((sum, d) => sum + d.Annual_Rainfall_mm, 0);
            const avg = (total / distData.length).toFixed(1);
            metricAvgRainfall.textContent = `${avg} mm`;
            metricAvgRainfallSub.textContent = `Based on ${distData.length} years`;
        } else {
            metricAvgRainfall.textContent = "-- mm";
        }

        // 2. Count events for selected year
        const yearEvents = EVENTS_DATA.filter(ev => ev.Year === selectedYear);
        metricTotalEvents.textContent = yearEvents.length;
        metricTotalEventsSub.textContent = `Documented in ${selectedYear}`;

        // 3. Wettest District for selected year
        const yearRainfall = RAINFALL_DATA.filter(d => d.Year === selectedYear);
        if (yearRainfall.length > 0) {
            const wettest = yearRainfall.reduce((max, d) => d.Annual_Rainfall_mm > max.Annual_Rainfall_mm ? d : max, yearRainfall[0]);
            metricWettestDistrict.textContent = wettest.District;
            metricWettestVal.textContent = `${wettest.Annual_Rainfall_mm.toFixed(1)} mm`;
        } else {
            metricWettestDistrict.textContent = "--";
            metricWettestVal.textContent = "-- mm";
        }
    }

    // --- CHARTS CONFIGURATION ---
    function getChartThemeColors() {
        const text = isDarkMode ? "#f8fafc" : "#1f2937";
        const grid = isDarkMode ? "rgba(255, 255, 255, 0.06)" : "rgba(0, 0, 0, 0.05)";
        return { text, grid };
    }

    function renderRainfallTrendChart() {
        const theme = getChartThemeColors();
        const distData = RAINFALL_DATA.filter(d => d.District === selectedDistrict)
                                     .sort((a, b) => a.Year - b.Year);
        
        const labels = distData.map(d => d.Year);
        const values = distData.map(d => d.Annual_Rainfall_mm);

        if (charts.trend) {
            charts.trend.destroy();
        }

        const ctx = document.getElementById("rainfallTrendChart").getContext("2d");
        
        // Gradient fill
        const gradient = ctx.createLinearGradient(0, 0, 0, 300);
        gradient.addColorStop(0, "rgba(6, 182, 212, 0.35)");
        gradient.addColorStop(1, "rgba(6, 182, 212, 0)");

        charts.trend = new Chart(ctx, {
            type: "line",
            data: {
                labels: labels,
                datasets: [{
                    label: `${selectedDistrict} Rainfall (mm)`,
                    data: values,
                    borderColor: "#06b6d4",
                    borderWidth: 3,
                    pointBackgroundColor: "#06b6d4",
                    pointHoverRadius: 7,
                    tension: 0.35,
                    fill: true,
                    backgroundColor: gradient
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { labels: { color: theme.text, font: { family: "Plus Jakarta Sans" } } }
                },
                scales: {
                    x: {
                        grid: { color: theme.grid },
                        ticks: { color: theme.text }
                    },
                    y: {
                        grid: { color: theme.grid },
                        ticks: { color: theme.text }
                    }
                }
            }
        });
    }

    function renderDistrictComparisonChart() {
        const theme = getChartThemeColors();
        const yearData = RAINFALL_DATA.filter(d => d.Year === selectedYear)
                                      .sort((a, b) => b.Annual_Rainfall_mm - a.Annual_Rainfall_mm);
        
        const labels = yearData.map(d => d.District);
        const values = yearData.map(d => d.Annual_Rainfall_mm);

        if (charts.comparison) {
            charts.comparison.destroy();
        }

        const ctx = document.getElementById("districtComparisonChart").getContext("2d");
        charts.comparison = new Chart(ctx, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: `Annual Rainfall (mm) - ${selectedYear}`,
                    data: values,
                    backgroundColor: values.map(v => v > 2000 ? "rgba(168, 85, 247, 0.75)" : "rgba(6, 182, 212, 0.75)"),
                    borderColor: values.map(v => v > 2000 ? "#a855f7" : "#06b6d4"),
                    borderWidth: 1,
                    borderRadius: 5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { labels: { color: theme.text, font: { family: "Plus Jakarta Sans" } } }
                },
                scales: {
                    x: {
                        grid: { display: false },
                        ticks: { color: theme.text, autoSkip: false, maxRotation: 45, minRotation: 45 }
                    },
                    y: {
                        grid: { color: theme.grid },
                        ticks: { color: theme.text }
                    }
                }
            }
        });
    }

    function renderEventDistributionChart() {
        const theme = getChartThemeColors();
        
        // Count category distributions globally
        const counts = { flood: 0, cyclone: 0, heatwave: 0, landslide: 0 };
        
        EVENTS_DATA.forEach(ev => {
            const cat = categorizeEvent(ev);
            if (counts[cat] !== undefined) {
                counts[cat]++;
            }
        });

        if (charts.distribution) {
            charts.distribution.destroy();
        }

        const ctx = document.getElementById("eventDistributionChart").getContext("2d");
        charts.distribution = new Chart(ctx, {
            type: "doughnut",
            data: {
                labels: ["Floods / Heavy Rain", "Cyclones / Storms", "Heat / Cold Waves", "Landslides"],
                datasets: [{
                    data: [counts.flood, counts.cyclone, counts.heatwave, counts.landslide],
                    backgroundColor: [
                        "rgba(6, 182, 212, 0.8)",
                        "rgba(168, 85, 247, 0.8)",
                        "rgba(249, 115, 22, 0.8)",
                        "rgba(239, 68, 68, 0.8)"
                    ],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { 
                        position: "bottom",
                        labels: { color: theme.text, font: { family: "Plus Jakarta Sans", size: 10 } } 
                    }
                },
                cutout: "65%"
            }
        });
    }

    // Helper to categorize based on text matches
    function categorizeEvent(ev) {
        const r = (ev.Rainfall || "").toLowerCase();
        const d = (ev.Damage || "").toLowerCase();
        const combined = `${r} ${d}`;
        
        if (combined.includes("cyclone") || combined.includes("squall") || combined.includes("storm") || combined.includes("wind")) {
            return "cyclone";
        }
        if (combined.includes("heat") || combined.includes("cold")) {
            return "heatwave";
        }
        if (combined.includes("landslide")) {
            return "landslide";
        }
        // Fallback or explicit mention of rain/flood
        return "flood";
    }

    // --- EVENTS TABLE RENDERING & FILTERING ---
    function renderEventsTable() {
        const query = searchInput.value.toLowerCase().trim();
        const typeFilter = eventTypeFilter.value;

        // Filter events
        const filtered = EVENTS_DATA.filter(ev => {
            const matchesQuery = ev.Place.toLowerCase().includes(query) || 
                                 ev.Damage.toLowerCase().includes(query) ||
                                 ev.Rainfall.toLowerCase().includes(query) ||
                                 ev.Year.toString().includes(query);
                                 
            const cat = categorizeEvent(ev);
            const matchesType = (typeFilter === "all" || cat === typeFilter);

            return matchesQuery && matchesType;
        });

        // Clear Table
        eventsTableBody.innerHTML = "";

        if (filtered.length === 0) {
            eventsTableBody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--text-muted);">No records found matching search criteria.</td></tr>`;
            tableInfoCount.textContent = `Showing 0 of ${EVENTS_DATA.length} records`;
            return;
        }

        // Render rows
        filtered.forEach(ev => {
            const tr = document.createElement("tr");
            const cat = categorizeEvent(ev);
            
            // Format labels beautifully
            const categoryLabel = {
                flood: "Floods & Heavy Rain",
                cyclone: "Cyclones & Storms",
                heatwave: "Heat / Cold Waves",
                landslide: "Landslides"
            }[cat];

            tr.innerHTML = `
                <td><strong>${ev.Year}</strong></td>
                <td>${ev.Place}</td>
                <td><span class="event-tag tag-${cat}">${categoryLabel}</span></td>
                <td>${ev.Damage || ev.Rainfall || "anomalous weather alerts"}</td>
            `;
            eventsTableBody.appendChild(tr);
        });

        tableInfoCount.textContent = `Showing ${filtered.length} of ${EVENTS_DATA.length} records`;
    }

    // --- EVENT HANDLERS & BINDINGS ---
    function setupEventListeners() {
        districtSelect.addEventListener("change", (e) => {
            selectedDistrict = e.target.value;
            document.getElementById("trend-badge").textContent = selectedDistrict;
            updateDashboard();
        });

        yearSelect.addEventListener("change", (e) => {
            selectedYear = parseInt(e.target.value);
            document.getElementById("comparison-badge").textContent = selectedYear;
            updateDashboard();
        });

        searchInput.addEventListener("input", renderEventsTable);
        eventTypeFilter.addEventListener("change", renderEventsTable);

        // Theme toggler
        themeToggleBtn.addEventListener("click", () => {
            isDarkMode = !isDarkMode;
            if (isDarkMode) {
                document.body.removeAttribute("data-theme");
                themeToggleBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';
            } else {
                document.body.setAttribute("data-theme", "light");
                themeToggleBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';
            }
            // Re-render charts with updated theme colors
            renderRainfallTrendChart();
            renderDistrictComparisonChart();
            renderEventDistributionChart();
        });
    }

    // Update charts & dynamic KPIs
    function updateDashboard() {
        updateDynamicMetrics();
        renderRainfallTrendChart();
        renderDistrictComparisonChart();
        renderEventDistributionChart();
        renderEventsTable();
    }

    // Launch Portal
    init();
});
