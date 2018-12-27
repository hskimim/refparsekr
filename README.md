# **Parsing_the_references**
_______________________________________________

Python package for parsing the academic references.

### Introduction
Academic paper we can get is formed as PDF or DOCS etc (.pdf , .docs)
This package can parse the references line by line by using `regular expression.`  

### Requirement
You need to install package named [pdfminer.six](https://pypi.org/project/pdfminer.six/)
you can also install easily the package as command line
```pip install pdfminer.six```

### Further task
I'm gonna make fine tuned version of package which can split the sentence into name , year , paper title , journal etc
### Install
```
pip install -e git+https://github.com/hskimim/refparsekr.git#egg=CA
```

### Example Code
```python
file_path = os.listdir("/home/hskimim/Documents/pdf_folder/")[0]
ref = Slicing_paper(file_path)
ref.split()
```
### Output
```
['김석진 김지영 “매각목적과 분리매각의 성과” 증권학회지 제32권 제1호 2003',
 '김원기 박춘광 “사업구조조정을 위한 자산매각과 Tobin’s Q” 재무관리연구 제16권 제1호 1999',
 '김지수 조정일 “분리설립의 기업성과와 성과요인” 재무관리 제18권 제2호 2005 139183. 김정애 “한국 주식시장에서 기업분할의 동기와 시사점” 주식 2003 제424호. 박성규 전수영 “기업분할의 공시효과와 기업특성” 회계정보연구 2008 제26권 제1호',
 'Alexander G. J. P. G. Benson and J. M. Kampmeyer “Investigating the valuation effects of announcements of voluntary divestitures ” The Journal of Finance 39(2) (1984)',
 'Comment R. and G. Jarrell “Corporate focus and stock returns ” Journal of Financial Economics 37 (1995)',
 'Cusatis P. J. J. A. Miles and J. R. Woolridge “Restructuring through spinoffs：the stock market evidence ” Journal of Financial Economics 33 (1993)',
 'Denning K. C. “Spin-offs and sales of assets：An examination of security returns and divestment motivations ” Accounting and Business Research 19 (1988)',
 'Desai H. and Jain P. “Firm performance and focus：Long-run stock market performance following spin-offs ” Journal of Financial Economics 54 (1999)',
 'Frank K. and J. Harden “Corporate Restructurings：A Comparison of Equity Carve-outs and Spin-offs ” Journal of Business Finance and Accounting 28 (2001)',
 'Hite G. L. and J. E. Owers “Security price reactions around corporate spin-off announcements ” Journal of Financial Economics 12 (1983)',
 'Jain P. C. “The effect of voluntary sell-off announcements on shareholder wealth ” The Journal of Finance 40(1) (1985)',
 'John K. and E. Ofek “Asset sales and increase in focus ” Journal of Financial Economics 37 (1995)',
 'Krishnaswami S. and V. Subramaniam “Information asymmetry valuation and the  기업분할 방법과 공시효과 79 corporate spin-off decision ” Journal of Financial Economics 53 (1999)',
 'Maydew E. L. K. Schipper and L. Vincent “The Impact of Taxes on the Choice of Divestiture Method ” Journal of Accounting Economics 28 (1999)',
 'Miles J. A. and J. D. Rosenfeld “The effect of voluntary spin-off announcements of shareholder wealth ” Journal of Finance 38(5) (1983)',
 'Schipper K. and A. Smith “Effects of recontracting on shareholder wealth：The case of voluntary spin-offs ” Journal of Financial Economics 12 (1983)',
 'Slovin M. M. Sushka and S. Ferraro “A comparison of the information conveyed by equity carve-outs spin-offs and asset sell-offs ” Journal of Financial Economics 37 (1995)',
 'Veld C. and Y. V. Veld-Merkoulova “Do spinoffs really create value? The European case ” Journal of Banking and Finance 28 (2004)']
```
