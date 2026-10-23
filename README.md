# XING Jobs Scraper - Stellenangebote, Salaries, New Jobs

XING jobs scraper for Germany, Austria and Switzerland: job title, company, location, salary range, employment type, career level and posting date from XING Stellenangebote. Monitor mode returns only new jobs since the last run. Plain HTTP, no login.

**[Run it on Apify Store](https://apify.com/kamerozkan/xing-jobs-scraper)**: no servers, no proxies to manage, results as JSON, CSV or Excel, or straight into your app through the API.

## Why use it

- Runs in the cloud on [Apify](https://apify.com/kamerozkan/xing-jobs-scraper); start it from the browser, the API, a schedule, or tools like Make, n8n and Zapier.
- Pay only for results. The current price and plan discounts are always on the [Store page](https://apify.com/kamerozkan/xing-jobs-scraper).
- Cap the cost of any run with the maximum cost per run setting.

## Quick start

1. Open the [Actor page](https://apify.com/kamerozkan/xing-jobs-scraper) and click **Try for free**.
2. Paste an input like the one below and click **Start**.
3. Download the dataset or read it over the API.

```json
{
  "queries": [
    "python developer"
  ],
  "location": "Berlin",
  "maxItems": 20
}
```

## Use it from code

Python ([examples/python_example.py](examples/python_example.py)), Node.js ([examples/node_example.js](examples/node_example.js)) and cURL ([examples/curl.sh](examples/curl.sh)) examples are in the `examples` folder. All of them need an [Apify API token](https://console.apify.com/settings/integrations).

## Sample output

Real rows from a recent run, with any contact details masked. Full sample: [sample-output.json](sample-output.json).

```json
[
  {
    "jobId": "158116665",
    "url": "https://www.xing.com/jobs/duesseldorf-sap-berater-financial-supply-chain-158116665",
    "title": "SAP Berater FI/CO (M/W/D)",
    "company": "BDF EXPERTS",
    "location": "Düsseldorf",
    "city": "Düsseldorf",
    "region": "Nordrhein-Westfalen",
    "postalCode": "40213",
    "country": "DE",
    "remote": true,
    "employmentType": "Full-time",
    "careerLevel": "Professional/Experienced",
    "industry": "Information services",
    "salaryMin": 50000,
    "salaryMax": 59000,
    "salaryCurrency": "EUR",
    "salaryPeriod": "YEAR",
    "salaryText": "€50,000 – €59,000",
    "salarySource": "job ad",
    "datePosted": "2026-09-24T14:50:04Z",
    "validThrough": "2026-11-23T14:50:06Z",
    "easyApply": true,
    "directApply": true,
    "descriptionText": "Werde zum Architekten digitaler Finanzwelten – und gestalte mit uns die Zukunft! Zahlen sind Deine Leidenschaft, die Financial Supply Chain und SAP FI/CO Dein Spielfeld? Perfekt! Denn als Consultant wirst Du:\nAufgaben\nDigitale Finanzwelten erschaffen – Du berätst und implementierst SAP FI/CO-Lösungen, die unsere Kunden begeistern\nGeschäftsprozesse neu denken – Du analysierst, designst und revolutionierst Finanzprozesse\nWissen teilen und multiplizieren – In Deinen Workshops und Schulungen machst Du aus Anwendern echte Power-User\nKonzepte entwickeln, die beeindrucken – Deine Fachkonzepte sind so klar wie durchdacht\nBestehende Lösungen auf das nächste Level heben – Du entwickelst SAP- und BDF-Lösungen kontinuierlich weiter\nQualifikation\nDu bist unser Perfect Match, wenn Du:\nEinen Abschluss in BWL, Wirtschaftsinformatik oder eine vergleichbare Qualifikation in der Tasche hast\nMindestens 3 Jahre Erfahrungen als SAP FI/CO-Berater gesammelt hast\nDie SAP-Module FI und CO oder FSCM bereits kennst und Dich dort weiter einarbeiten möchtest\nErfahrungen im SAP-Customizing sammeln konntest\nKomplexe Zusammenhänge schnell erfasst und in klare Konzepte übersetzt\nNicht nur mit Zahlen, sondern auch mit Menschen hervorragend kommunizieren kannst\nAuf Deutsch und Englisch überzeugst – egal ob in Meetings oder Dokumentationen\nDen Kunden immer in den Mittelpunkt stellst und flexibel auf Anforderungen reagierst\nBereit bist, gelegentlich zu reisen (keine Sorge, wir schicken Dich nicht auf Weltreise)\nErfahrungen und Interesse an der Erarbeitung von KI Use Cases hast\nBenefits\nBei uns erwartet Dich mehr als nur ein Job:\nAbwechslung garantiert! Kein Tag gleicht dem anderen in unserem dynamischen Team\nWork-Life-Balance leben mit flexiblen Arbeitszeiten und Homeoffice-Möglichkeiten\nWachse über Dich hinaus durch individuelle Weiterbildungen, die zu Dir passen\nIdeen statt Hierarchien – bei uns zählt Dein Input, nicht Dein Titel\nGestalte aktiv mit und sieh, wie Deine Ideen Wirklichkeit werden\nHeute Consultant, morgen...? Bei uns kannst Du:\nEinen langfristigen Karriereweg einschlagen – vielleicht als zukünftiger Projektleiter oder Solution Specialist\nTei
```

## Support

Found a problem or need a field? Open an issue on the [Actor's Issues tab](https://apify.com/kamerozkan/xing-jobs-scraper/issues) and include your run link.

---
This repository holds usage examples and sample data. The Actor itself runs on Apify.
