# 🌍 World Bank Data Visualizer

**An Interactive Global Development Indicators Visualization Platform**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![Data Source](https://img.shields.io/badge/Data%20Source-World%20Bank%20API-blue)](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/deluair/WB_visuals)

> Transform complex global development data into intuitive, interactive visualizations. Explore nearly **16,000 time series indicators** from over **45 World Bank databases** with professional-grade mapping and analytics tools.

![World Bank Data Visualizer Demo](https://via.placeholder.com/800x400/1e3a8a/ffffff?text=World+Bank+Data+Visualizer)

## ✨ Key Features

### 🎯 **Interactive Global Mapping**
- **Real-time World Bank API Integration** using [v2 endpoints](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
- **195+ Countries** with precise geographic coordinates
- **Responsive Circle Markers** with proportional sizing based on data values
- **Smart Auto-Zoom** for selected countries and regions

### 📊 **Rich Data Visualization**
- **10 Key Development Indicators** including GDP, Population, Life Expectancy, and more
- **5 Professional Color Schemes** (Blues, Reds, Greens, Purples, Oranges)
- **3 Statistical Classification Methods** (Quantile, Equal Interval, Natural Breaks)
- **Adjustable Marker Sizes** (Small, Medium, Large, Extra Large)

### 🎛️ **Advanced Controls**
- **Individual Country Selection** with flag emojis and alphabetical sorting
- **Regional Filtering** (Africa, Asia, Europe, Americas, etc.)
- **Toggle Country Labels** for immediate identification
- **Smart Map Navigation** with fit-to-data and reset zoom functions

### 📈 **Professional Analytics**
- **Real-time Statistics** (Count, Min, Max, Mean, Median)
- **Interactive Legend** with value ranges and color coding
- **Enhanced Popups** with flags, coordinates, and detailed information
- **CSV Data Export** for further analysis

## 🚀 Quick Start

### Prerequisites
- **Python 3.6+** (for local development server)
- **Modern Web Browser** (Chrome, Firefox, Safari, Edge)
- **Internet Connection** (for World Bank API access)

### Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/deluair/WB_visuals.git
   cd WB_visuals
   ```

2. **Start the Development Server**
   ```bash
   python server.py
   ```
   
3. **Open in Browser**
   - The application will automatically open at `http://localhost:8000`
   - Or manually navigate to the URL in your browser

### Alternative: Direct Browser Access
Simply open `index.html` directly in your web browser for immediate access without a server.

## 📋 Available Indicators

| Indicator | Code | Description |
|-----------|------|-------------|
| 📊 **Population, Total** | `SP.POP.TOTL` | Total population count |
| 💰 **GDP (Current US$)** | `NY.GDP.MKTP.CD` | Gross Domestic Product in current US dollars |
| 💵 **GDP Per Capita** | `NY.GDP.PCAP.CD` | GDP divided by midyear population |
| 🏥 **Life Expectancy** | `SP.DYN.LE00.IN` | Life expectancy at birth, total years |
| 📚 **Literacy Rate** | `SE.ADT.LITR.ZS` | Literacy rate, adult total (% of people ages 15+) |
| 👶 **Child Mortality** | `SH.DYN.MORT` | Mortality rate, under-5 per 1,000 live births |
| 🌱 **CO2 Emissions** | `EN.ATM.CO2E.PC` | CO2 emissions (metric tons per capita) |
| ⚡ **Electric Power** | `EG.USE.ELEC.KH.PC` | Electric power consumption (kWh per capita) |
| 💻 **Internet Users** | `IT.NET.USER.ZS` | Internet users (% of population) |
| 💼 **Unemployment** | `SL.UEM.TOTL.ZS` | Unemployment, total (% of total labor force) |

## 🎨 Visualization Options

### Color Schemes
- 🔵 **Blues**: Professional, data-focused visualization
- 🔴 **Reds**: High-impact, attention-drawing maps
- 🟢 **Greens**: Environmental and growth indicators
- 🟣 **Purples**: Sophisticated, modern appearance
- 🟠 **Oranges**: Warm, engaging visualization

### Classification Methods
- **📊 Quantile**: Equal number of countries per class
- **📏 Equal Interval**: Equal value ranges per class
- **🎯 Natural Breaks**: Data-driven optimal groupings

### Marker Sizes
- **🔸 Small**: Subtle, high-density visualizations
- **🔹 Medium**: Balanced visibility (default)
- **🔶 Large**: Enhanced visibility for presentations
- **🔷 Extra Large**: Maximum impact for demonstrations

## 🛠️ Technical Architecture

### Frontend Technologies
- **HTML5** with semantic structure
- **CSS3** with responsive Bootstrap 5 framework
- **JavaScript ES6+** with modern async/await patterns
- **Leaflet.js** for interactive mapping
- **OpenStreetMap** tiles for base mapping

### Data Integration
- **World Bank API v2** for real-time data access
- **RESTful API calls** with proper error handling
- **JSON data parsing** and validation
- **Fallback mechanisms** for offline functionality

### Performance Features
- **Lazy Loading** of country data
- **Efficient Marker Rendering** with LayerGroups
- **Smart Bounds Calculation** for optimal map views
- **Memory Management** with layer cleanup

## 📊 Usage Examples

### Basic Workflow
1. **Select Region**: Choose global view or specific region
2. **Choose Country**: Optional individual country selection
3. **Pick Indicator**: Select from 10 development metrics
4. **Set Year**: Choose from 2018-2022 data
5. **Customize Display**: Adjust colors, sizes, and classification
6. **Load Data**: Click "🚀 Load Data" to visualize
7. **Explore Results**: Interact with markers and view statistics

### Advanced Features
- **🎯 Fit to Data**: Automatically zoom to data bounds
- **🌍 Reset Zoom**: Return to global view
- **🏷️ Toggle Labels**: Show/hide country codes
- **📁 Export Data**: Download results as CSV

### Example Use Cases
- **📈 Economic Analysis**: Compare GDP per capita across regions
- **🏥 Health Research**: Analyze life expectancy trends
- **🌱 Environmental Studies**: Examine CO2 emissions patterns
- **📚 Education Assessment**: Review literacy rates globally
- **💻 Digital Divide**: Explore internet penetration data

## 🔧 Customization

### Adding New Indicators
1. Add indicator to the `indicatorSelect` dropdown in `index.html`
2. Include appropriate emoji and description
3. Test data availability via World Bank API

### Extending Color Schemes
```javascript
this.colorSchemes.newScheme = [
    '#color1', '#color2', '#color3', 
    '#color4', '#color5', '#color6', 
    '#color7', '#color8'
];
```

### Custom Country Coordinates
Update the `countryCoordinates` object with new country entries:
```javascript
'NEW': [latitude, longitude]
```

## 📱 Browser Compatibility

| Browser | Version | Support |
|---------|---------|---------|
| **Chrome** | 80+ | ✅ Full Support |
| **Firefox** | 75+ | ✅ Full Support |
| **Safari** | 13+ | ✅ Full Support |
| **Edge** | 80+ | ✅ Full Support |
| **Mobile** | Modern | ✅ Responsive |

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the Repository**
2. **Create Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Commit Changes**: `git commit -m 'Add amazing feature'`
4. **Push to Branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

### Development Guidelines
- Follow existing code style and structure
- Test all new features thoroughly
- Update documentation for new functionality
- Ensure cross-browser compatibility

## 📄 API Reference

### World Bank API Endpoints
- **Countries**: `https://api.worldbank.org/v2/country`
- **Indicators**: `https://api.worldbank.org/v2/country/{country}/indicator/{indicator}`
- **Documentation**: [World Bank API Guide](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392)

### Rate Limits
- No authentication required
- No explicit rate limits
- Respectful usage recommended

## 🔍 Troubleshooting

### Common Issues

**Data Not Loading**
- Check internet connection
- Verify World Bank API accessibility
- Try different year or indicator

**Map Not Displaying**
- Ensure JavaScript is enabled
- Check browser console for errors
- Verify Leaflet.js library loading

**Performance Issues**
- Use smaller marker sizes for large datasets
- Select specific regions instead of global data
- Clear browser cache

## 📈 Performance Metrics

- **Load Time**: < 3 seconds for typical queries
- **Data Coverage**: 195+ countries supported
- **Response Time**: < 2 seconds for API calls
- **Memory Usage**: Optimized for large datasets

## 🔗 Related Resources

- **[World Bank Open Data](https://data.worldbank.org/)**: Official data portal
- **[Leaflet Documentation](https://leafletjs.com/)**: Mapping library guide
- **[Bootstrap 5](https://getbootstrap.com/)**: UI framework documentation
- **[World Bank API](https://datahelpdesk.worldbank.org/)**: Complete API documentation

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/deluair/WB_visuals/issues)
- **Discussions**: [GitHub Discussions](https://github.com/deluair/WB_visuals/discussions)
- **Documentation**: This README and inline code comments

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **World Bank Group** for providing open access to development data
- **OpenStreetMap** contributors for mapping data
- **Leaflet.js** community for the excellent mapping library
- **Bootstrap** team for the responsive UI framework

---

<div align="center">

**🌍 Transforming Data into Insights • Built with ❤️ for Global Development**

[🚀 Try Live Demo](http://localhost:8000) • [📊 World Bank Data](https://data.worldbank.org/) • [🔧 API Docs](https://datahelpdesk.worldbank.org/)

</div> 