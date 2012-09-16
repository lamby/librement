from django_enumfield import Item, make_enum

AccountEnum = make_enum('AccountEnum',
    Item(0, 'individual', "Individual"),
    Item(1, 'company', "Company"),
    Item(2, 'non_profit', "Non-profit"),
)

CountryEnum = make_enum('CountryEnum',
    Item(1, 'af', "Afghanistan"),
    Item(2, 'al', "Albania"),
    Item(3, 'dz', "Algeria"),
    Item(4, 'as', "American Samoa"),
    Item(5, 'ad', "Andorra"),
    Item(6, 'ao', "Angola"),
    Item(7, 'ai', "Anguilla"),
    Item(8, 'aq', "Antarctica"),
    Item(9, 'ag', "Antigua And Barbuda"),
    Item(10, 'ar', "Argentina"),
    Item(11, 'am', "Armenia"),
    Item(12, 'aw', "Aruba"),
    Item(13, 'au', "Australia"),
    Item(14, 'at', "Austria"),
    Item(15, 'az', "Azerbaijan"),
    Item(16, 'bs', "Bahamas"),
    Item(17, 'bh', "Bahrain"),
    Item(18, 'bd', "Bangladesh"),
    Item(19, 'bb', "Barbados"),
    Item(20, 'by', "Belarus"),
    Item(21, 'be', "Belgium"),
    Item(22, 'bz', "Belize"),
    Item(23, 'bj', "Benin"),
    Item(24, 'bm', "Bermuda"),
    Item(25, 'bt', "Bhutan"),
    Item(26, 'bo', "Bolivia"),
    Item(27, 'ba', "Bosnia And Herzegovina"),
    Item(28, 'bw', "Botswana"),
    Item(29, 'br', "Brazil"),
    Item(30, 'io', "British Indian Ocean Territory"),
    Item(31, 'bn', "Brunei Darussalam"),
    Item(32, 'bg', "Bulgaria"),
    Item(33, 'bf', "Burkina Faso"),
    Item(34, 'bi', "Burundi"),
    Item(35, 'kh', "Cambodia"),
    Item(36, 'cm', "Cameroon"),
    Item(37, 'ca', "Canada"),
    Item(38, 'cv', "Cape Verde"),
    Item(39, 'ky', "Cayman Islands"),
    Item(40, 'cf', "Central African Republic"),
    Item(41, 'td', "Chad"),
    Item(42, 'cl', "Chile"),
    Item(43, 'cn', "China"),
    Item(44, 'co', "Colombia"),
    Item(45, 'km', "Comoros"),
    Item(46, 'cg', "Congo"),
    Item(47, 'ck', "Cook Islands"),
    Item(48, 'cr', "Costa Rica"),
    Item(49, 'ci', "Cote D'Ivoire"),
    Item(50, 'hr', "Croatia"),
    Item(51, 'cu', "Cuba"),
    Item(52, 'cy', "Cyprus"),
    Item(53, 'cz', "Czech Republic"),
    Item(54, 'dk', "Denmark"),
    Item(55, 'dj', "Djibouti"),
    Item(56, 'dm', "Dominica"),
    Item(57, 'do', "Dominican Republic"),
    Item(58, 'ec', "Ecuador"),
    Item(59, 'eg', "Egypt"),
    Item(60, 'sv', "El Salvador"),
    Item(61, 'gq', "Equatorial Guinea"),
    Item(62, 'er', "Eritrea"),
    Item(63, 'ee', "Estonia"),
    Item(64, 'et', "Ethiopia"),
    Item(65, 'fk', "Falkland Islands (Malvinas)"),
    Item(66, 'fo', "Faroe Islands"),
    Item(67, 'fm', "Federated States Of Micronesia"),
    Item(68, 'fj', "Fiji"),
    Item(69, 'fi', "Finland"),
    Item(70, 'fr', "France"),
    Item(71, 'gf', "French Guiana"),
    Item(72, 'pf', "French Polynesia"),
    Item(73, 'ga', "Gabon"),
    Item(74, 'gm', "Gambia"),
    Item(75, 'ge', "Georgia"),
    Item(76, 'de', "Germany"),
    Item(77, 'gh', "Ghana"),
    Item(78, 'gi', "Gibraltar"),
    Item(79, 'gr', "Greece"),
    Item(80, 'gl', "Greenland"),
    Item(81, 'gd', "Grenada"),
    Item(82, 'gp', "Guadeloupe"),
    Item(83, 'gu', "Guam"),
    Item(84, 'gt', "Guatemala"),
    Item(85, 'gn', "Guinea"),
    Item(86, 'gw', "Guinea-Bissau"),
    Item(87, 'gy', "Guyana"),
    Item(88, 'ht', "Haiti"),
    Item(89, 'va', "Holy See (Vatican City State)"),
    Item(90, 'hn', "Honduras"),
    Item(91, 'hk', "Hong Kong"),
    Item(92, 'hu', "Hungary"),
    Item(93, 'is', "Iceland"),
    Item(94, 'in', "India"),
    Item(95, 'id', "Indonesia"),
    Item(96, 'iq', "Iraq"),
    Item(97, 'ie', "Ireland"),
    Item(98, 'ir', "Islamic Republic Of Iran"),
    Item(99, 'il', "Israel"),
    Item(100, 'it', "Italy"),
    Item(101, 'jm', "Jamaica"),
    Item(102, 'jp', "Japan"),
    Item(103, 'jo', "Jordan"),
    Item(104, 'kz', "Kazakhstan"),
    Item(105, 'ke', "Kenya"),
    Item(106, 'ki', "Kiribati"),
    Item(107, 'kw', "Kuwait"),
    Item(108, 'kg', "Kyrgyzstan"),
    Item(109, 'la', "Lao People's Democratic Republic"),
    Item(110, 'lv', "Latvia"),
    Item(111, 'lb', "Lebanon"),
    Item(112, 'ls', "Lesotho"),
    Item(113, 'lr', "Liberia"),
    Item(114, 'ly', "Libyan Arab Jamahiriya"),
    Item(115, 'li', "Liechtenstein"),
    Item(116, 'lt', "Lithuania"),
    Item(117, 'lu', "Luxembourg"),
    Item(118, 'mo', "Macao"),
    Item(119, 'mg', "Madagascar"),
    Item(120, 'mw', "Malawi"),
    Item(121, 'my', "Malaysia"),
    Item(122, 'mv', "Maldives"),
    Item(123, 'ml', "Mali"),
    Item(124, 'mt', "Malta"),
    Item(125, 'mh', "Marshall Islands"),
    Item(126, 'mq', "Martinique"),
    Item(127, 'mr', "Mauritania"),
    Item(128, 'mu', "Mauritius"),
    Item(129, 'yt', "Mayotte"),
    Item(130, 'mx', "Mexico"),
    Item(131, 'mc', "Monaco"),
    Item(132, 'mn', "Mongolia"),
    Item(231, 'me', "Montenegro"),
    Item(133, 'ms', "Montserrat"),
    Item(134, 'ma', "Morocco"),
    Item(135, 'mz', "Mozambique"),
    Item(136, 'mm', "Myanmar"),
    Item(137, 'na', "Namibia"),
    Item(138, 'nr', "Nauru"),
    Item(139, 'np', "Nepal"),
    Item(140, 'nl', "Netherlands"),
    Item(141, 'an', "Netherlands Antilles"),
    Item(142, 'nc', "New Caledonia"),
    Item(143, 'nz', "New Zealand"),
    Item(144, 'ni', "Nicaragua"),
    Item(145, 'ne', "Niger"),
    Item(146, 'ng', "Nigeria"),
    Item(147, 'nu', "Niue"),
    Item(148, 'nf', "Norfolk Island"),
    Item(149, 'mp', "Northern Mariana Islands"),
    Item(150, 'no', "Norway"),
    Item(151, 'om', "Oman"),
    Item(152, 'pk', "Pakistan"),
    Item(153, 'pw', "Palau"),
    Item(154, 'ps', "Palestinian Territory, Occupied"),
    Item(155, 'pa', "Panama"),
    Item(156, 'pg', "Papua New Guinea"),
    Item(157, 'py', "Paraguay"),
    Item(158, 'pe', "Peru"),
    Item(159, 'ph', "Philippines"),
    Item(160, 'pl', "Poland"),
    Item(161, 'pt', "Portugal"),
    Item(162, 'pr', "Puerto Rico"),
    Item(163, 'qa', "Qatar"),
    Item(164, 'kr', "Republic Of Korea"),
    Item(165, 'md', "Republic Of Moldova"),
    Item(166, 're', "Reunion"),
    Item(167, 'ro', "Romania"),
    Item(168, 'ru', "Russian Federation"),
    Item(169, 'rw', "Rwanda"),
    Item(170, 'kn', "Saint Kitts And Nevis"),
    Item(171, 'lc', "Saint Lucia"),
    Item(172, 'vc', "Saint Vincent And The Grenadines"),
    Item(173, 'ws', "Samoa"),
    Item(174, 'sm', "San Marino"),
    Item(175, 'st', "Sao Tome And Principe"),
    Item(176, 'sa', "Saudi Arabia"),
    Item(177, 'sn', "Senegal"),
    Item(232, 'rs', "Serbia"),
    Item(179, 'sc', "Seychelles"),
    Item(180, 'sl', "Sierra Leone"),
    Item(181, 'sg', "Singapore"),
    Item(182, 'sk', "Slovakia"),
    Item(183, 'si', "Slovenia"),
    Item(184, 'sb', "Solomon Islands"),
    Item(185, 'so', "Somalia"),
    Item(186, 'za', "South Africa"),
    Item(187, 'gs', "South Georgia"),
    Item(233, 'ss', "South Sudan"),
    Item(188, 'es', "Spain"),
    Item(189, 'lk', "Sri Lanka"),
    Item(190, 'sd', "Sudan"),
    Item(191, 'sr', "Suriname"),
    Item(192, 'sz', "Swaziland"),
    Item(193, 'se', "Sweden"),
    Item(194, 'ch', "Switzerland"),
    Item(195, 'sy', "Syrian Arab Republic"),
    Item(196, 'tw', "Taiwan"),
    Item(197, 'tj', "Tajikistan"),
    Item(198, 'th', "Thailand"),
    Item(199, 'cd', "Republic Of Congo"),
    Item(200, 'mk', "Macedonia"),
    Item(201, 'tl', "Timor-Leste"),
    Item(202, 'tg', "Togo"),
    Item(203, 'tk', "Tokelau"),
    Item(204, 'to', "Tonga"),
    Item(205, 'tt', "Trinidad And Tobago"),
    Item(206, 'tn', "Tunisia"),
    Item(207, 'tr', "Turkey"),
    Item(208, 'tm', "Turkmenistan"),
    Item(209, 'tv', "Tuvalu"),
    Item(210, 'ug', "Uganda"),
    Item(211, 'ua', "Ukraine"),
    Item(212, 'ae', "United Arab Emirates"),
    Item(213, 'gb', "United Kingdom"),
    Item(214, 'tz', "United Republic Of Tanzania"),
    Item(215, 'us', "United States"),
    Item(216, 'um', "United States Minor Outlying Islands"),
    Item(217, 'uy', "Uruguay"),
    Item(218, 'uz', "Uzbekistan"),
    Item(219, 'vu', "Vanuatu"),
    Item(220, 've', "Venezuela"),
    Item(221, 'vn', "Viet Nam"),
    Item(222, 'vg', "Virgin Islands, British"),
    Item(223, 'vi', "Virgin Islands, U.S."),
    Item(224, 'wf', "Wallis And Futuna"),
    Item(225, 'ye', "Yemen"),
    Item(226, 'zm', "Zambia"),
    Item(227, 'zw', "Zimbabwe"),
)
