# Simple example

We include two whitepapers in the repository as examples for using
paper-analyser to pass papers and get results out.

To try the tool, simply follow the commands:
```
cd paper-analyzer
. venv/bin/activate
python3 ./pq_main.py -f ./example-papers/
```

At this point you will see results in `pq-out/out-0`

Specifically, you will see:
```
$ ls pq-out/out-0/
data_out  img  json_data  normalised_dependency_graph.json  parsed_paper_data.json  report.txt
```

* `data_out` contains one `.txt` and one `.xml` file for each PDF. These `.txt` and `.xml` are simply data representations of the content of the given PDF file.
* `json_data` contains JSON data representations for each paper
* `img` contains a `.png` image of a citation-dependency graph of the PDF files in the folder
* `parsed_paper_data.json` is a single json file containing data about the papers analysed, such as the title of each paper as well as the papers cited by each paper.
* `report.txt` contains a lot of information about the papers in data set

```
$ cat pq-out/out-0/report.txt
######################################
 Parsed papers summary        
paper:
    pq-out/out-0/json_data/json_dump_0.json
    b'A characterisation of system-wide propagation in the malware landscape '
    Normalised title: acharacterisationofsystemwidepropagationinthemalwarelandscape
    References:
        Authors:  Andrei Bacs, Remco Vermeulen, Asia Slowinska, and Herbert Bos
        Title:  System- Level Support for Intrusion Recovery
        Normalised: systemlevelsupportforintrusionrecovery
        -------------------
        Authors:  Thomas Barabosch, Niklas Bergmann, Adrian Dombeck, and Elmar Padilla
        Title:  Quincy: Detecting Host-Based Code Injection Attacks in Memory Dumps
        Normalised: quincy:detectinghostbasedcodeinjectionattacksinmemorydumps
        -------------------
        Authors:  Thomas Barabosch, Sebastian Eschweiler, and Elmar Gerhards-Padilla
        Title:  Bee Master: Detecting Host-Based Code Injection Attacks
        Normalised: beemaster:detectinghostbasedcodeinjectionattacks
        -------------------
        Authors:  Thomas Barabosch and Elmar Gerhards-Padilla
        Title:  Host-based code injection attacks: A popular technique used by malware
        Normalised: hostbasedcodeinjectionattacks:apopulartechniqueusedbymalware
        -------------------
        Authors:  Ulrich Bayer, Imam Habibi, Davide Balzarotti, and Engin Kirda
        Title:  A View on Current Malware Behaviors
        Normalised: aviewoncurrentmalwarebehaviors
        -------------------
        Authors:  Ulrich Bayer, Andreas Moser, Christopher Kruegel, and Engin Kirda
        Title:  Dy- namic Analysis of Malicious Code
        Normalised: dynamicanalysisofmaliciouscode
        -------------------
        Authors:  Magal Baz and Or Safran
        Title:  Dridexs Cold War: Enter AtomBombing
        Normalised: dridexscoldwar:enteratombombing
        -------------------
        Authors:  Fabrice Bellard
        Title:  QEMU, a Fast and Portable Dynamic Translator
        Normalised: qemuafastandportabledynamictranslator
        -------------------
        Authors:  Guillaume Bonfante, Jose Fernandez, Jean-Yves Marion, Benjamin Rouxel, Fab- rice Sabatier, and Aurelien Thierry
        Title:  CoDisasm: Medium Scale Con- catic Disassembly of Self-Modifying Binaries with Overlapping Instructions
        Normalised: codisasm:mediumscaleconcaticdisassemblyofselfmodifyingbinarieswithoverlappinginstructions
        -------------------
        Authors:  Brendan Dolan-Gavitt, Josh Hodosh, Patrick Hulin, Tim Leek, and Ryan Whelan
        Title:  Repeatable Reverse Engineering with PANDA
        Normalised: repeatablereverseengineeringwithpanda
        -------------------
        Authors:  Manuel Egele, Theodoor Scholte, Engin Kirda, and Christopher Kruegel
        Title:  A Survey on Automated Dynamic Malware-analysis Techniques and Tools
        Normalised: asurveyonautomateddynamicmalwareanalysistechniquesandtools
        -------------------
        Authors:  Adrienne Porter Felt, Matthew Finifter, Erika Chin, Steve Hanna, and David Wagner
        Title:  A Survey of Mobile Malware in the Wild
        Normalised: asurveyofmobilemalwareinthewild
        -------------------
        Authors:  Andrew Henderson, Lok-Kwong Yan, Xunchao Hu, Aravind Prakash, Heng Yin, and Stephen McCamant
        Title:  DECAF: A Platform-Neutral Whole-System Dynamic Binary Analysis Platform
        Normalised: decaf:aplatformneutralwholesystemdynamicbinaryanalysisplatform
        -------------------
        Authors:  Min Gyung Kang, Pongsin Poosankam, and Heng Yin
        Title:  Renovo: A Hidden Code Extractor for Packed Executables
        Normalised: renovo:ahiddencodeextractorforpackedexecutables
        -------------------
        Authors:  Yuhei Kawakoya, Eitaro Shioji, Makoto Iwamura, and Jun Miyoshi
        Title:  API Chaser: Taint-Assisted Sandbox for Evasive Malware Analysis
        Normalised: apichaser:taintassistedsandboxforevasivemalwareanalysis
        -------------------
        Authors:  David Korczynski
        Title:  RePEconstruct: reconstructing binaries with self- modifying code and import address table destruction
        Normalised: repeconstruct:reconstructingbinarieswithselfmodifyingcodeandimportaddresstabledestruction
        -------------------
        Authors:  David Korczynski
        Title:  Precise system-wide concatic malware unpacking
        Normalised: precisesystemwideconcaticmalwareunpacking
        -------------------
        Authors:  David Korczynski and Heng Yin
        Title:  Capturing Malware Propagations with Code Injections and Code-Reuse Attacks
        Normalised: capturingmalwarepropagationswithcodeinjectionsandcodereuseattacks
        -------------------
        Authors:  Kimberly Tam, Ali Feizollah, Nor Badrul Anuar, Rosli Salleh, and Lorenzo Caval- laro
        Title:  The Evolution of Android Malware and Android Analysis Techniques
        Normalised: theevolutionofandroidmalwareandandroidanalysistechniques
        -------------------
        Authors:  Heng Yin, Dawn Song, Manuel Egele, Christopher Kruegel, and Engin Kirda
        Title:  Panorama: Capturing System-wide Information Flow for Malware De- tection and Analysis
        Normalised: panorama:capturingsystemwideinformationflowformalwaredetectionandanalysis
        -------------------
        Authors:  Yajin Zhou and Xuxian Jiang
        Title:  Dissecting Android Malware: Character- ization and Evolution
        Normalised: dissectingandroidmalware:characterizationandevolution
        -------------------
paper:
    pq-out/out-0/json_data/json_dump_1.json
    b'Precise system-wide concatic malware unpacking '
    Normalised title: precisesystemwideconcaticmalwareunpacking
    References:
        Authors:  Andrei Bacs, Remco Vermeulen, Asia Slowinska, and Herbert Bos
        Title:  System- Level Support for Intrusion Recovery
        Normalised: systemlevelsupportforintrusionrecovery
        -------------------
        Authors:  G. Balakrishnan, T. Reps, D. Melski, and T. Teitelbaum
        Title:  WYSINWYX: What You See Is Not What You eXecute
        Normalised: wysinwyx:whatyouseeisnotwhatyouexecute
        -------------------
        Authors:  Tiffany Bao, Jonathan Burket, Maverick Woo, Rafael Turner, and David Brumley
        Title:  BYTEWEIGHT: Learning to Recognize Functions in Binary Code
        Normalised: byteweight:learningtorecognizefunctionsinbinarycode
        -------------------
        Authors:  Thomas Barabosch, Niklas Bergmann, Adrian Dombeck, and Elmar Padilla
        Title:  Quincy: Detecting Host-Based Code Injection Attacks in Memory Dumps
        Normalised: quincy:detectinghostbasedcodeinjectionattacksinmemorydumps
        -------------------
        Authors:  Thomas Barabosch, Sebastian Eschweiler, and Elmar Gerhards-Padilla
        Title:  Bee Master: Detecting Host-Based Code Injection Attacks
        Normalised: beemaster:detectinghostbasedcodeinjectionattacks
        -------------------
        Authors:  Guillaume Bonfante, Jose Fernandez, Jean-Yves Marion, Benjamin Rouxel, Fab- rice Sabatier, and Aurelien Thierry
        Title:  CoDisasm: Medium Scale Con- catic Disassembly of Self-Modifying Binaries with Overlapping Instructions
        Normalised: codisasm:mediumscaleconcaticdisassemblyofselfmodifyingbinarieswithoverlappinginstructions
        -------------------
        Authors:  Erik Bosman, Asia Slowinska, and Herbert Bos
        Title:  Minemu: The Worlds Fastest Taint Tracker
        Normalised: minemu:theworldsfastesttainttracker
        -------------------
        Could not parse
        -------------------
        Authors:  Cristina Cifuentes and K. John Gough
        Title:  Decompilation of Binary Pro- grams
        Normalised: decompilationofbinaryprograms
        -------------------
        Authors:  Artem Dinaburg, Paul Royal, Monirul Sharif, and Wenke Lee
        Title:  Ether: Malware Analysis via Hardware Virtualization Extensions
        Normalised: ether:malwareanalysisviahardwarevirtualizationextensions
        -------------------
        Authors:  Brendan Dolan-Gavitt, Josh Hodosh, Patrick Hulin, Tim Leek, and Ryan Whelan
        Title:  Repeatable Reverse Engineering with PANDA
        Normalised: repeatablereverseengineeringwithpanda
        -------------------
        Authors:  Thomas Dullien and Rolf Rolles
        Title:  Graph-based comparison of executable  objects (english version)
        Normalised: graphbasedcomparisonofexecutableobjects(englishversion)
        -------------------
        Authors:  Mike Van Emmerik
        Title:  Signatures for Library Functions in Executable Files
        Normalised: signaturesforlibraryfunctionsinexecutablefiles
        -------------------
        Authors:  Halvar Flake
        Title:  Structural Comparison of Executable Objects
        Normalised: structuralcomparisonofexecutableobjects
        -------------------
        Authors:  Fanglu Guo, Peter Ferrie, and Tzi-cker Chiueh
        Title:  A Study of the Packer Problem and Its Solutions
        Normalised: astudyofthepackerproblemanditssolutions
        -------------------
        Authors:  Andrew Henderson, Lok-Kwong Yan, Xunchao Hu, Aravind Prakash, Heng Yin, and Stephen McCamant
        Title:  DECAF: A Platform-Neutral Whole-System Dynamic Binary Analysis Platform
        Normalised: decaf:aplatformneutralwholesystemdynamicbinaryanalysisplatform
        -------------------
        Authors:  Xin Hu, Sandeep Bhatkar, Kent Griffin, and Kang G. Shin
        Title:  MutantX-S: Scalable Malware Clustering Based on Static Features
        Normalised: mutantxs:scalablemalwareclusteringbasedonstaticfeatures
        -------------------
        Authors:  Thomas Hungenberg and Matthias Eckert
        Title:  http://www
        Normalised: http://www
        -------------------
        Authors:  Kyriakos K. Ispoglou and Mathias Payer
        Title:  malWASH: Washing Malware to Evade Dynamic Analysis
        Normalised: malwash:washingmalwaretoevadedynamicanalysis
        -------------------
        Authors:  Emily R. Jacobson, Nathan Rosenblum, and Barton P. Miller
        Title:  Labeling Library Functions in Stripped Binaries
        Normalised: labelinglibraryfunctionsinstrippedbinaries
        -------------------
        Authors:  Sebastien Josse
        Title:  Secure and advanced unpacking using computer emulation
        Normalised: secureandadvancedunpackingusingcomputeremulation
        -------------------
        Authors:  S. Josse
        Title:  Malware Dynamic Recompilation
        Normalised: malwaredynamicrecompilation
        -------------------
        Authors:  Min Gyung Kang, Pongsin Poosankam, and Heng Yin
        Title:  Renovo: A Hidden Code Extractor for Packed Executables
        Normalised: renovo:ahiddencodeextractorforpackedexecutables
        -------------------
        Authors:  Yuhei Kawakoya, Makoto Iwamura, and Jun Miyoshi
        Title:  Taint-assisted IAT Reconstruction against Position Obfuscation
        Normalised: taintassistediatreconstructionagainstpositionobfuscation
        -------------------
        Authors:  Yuhei Kawakoya, Eitaro Shioji, Makoto Iwamura, and Jun Miyoshi
        Title:  API Chaser: Taint-Assisted Sandbox for Evasive Malware Analysis
        Normalised: apichaser:taintassistedsandboxforevasivemalwareanalysis
        -------------------
        Could not parse
        -------------------
        Authors:  Clemens Kolbitsch, Engin Kirda, and Christopher Kruegel
        Title:  The Power of Procrastination: Detection and Mitigation of Execution-stalling Malicious Code
        Normalised: thepowerofprocrastination:detectionandmitigationofexecutionstallingmaliciouscode
        -------------------
        Authors:  David Korczynski
        Title:  RePEconstruct: reconstructing binaries with self- modifying code and import address table destruction
        Normalised: repeconstruct:reconstructingbinarieswithselfmodifyingcodeandimportaddresstabledestruction
        -------------------
        Authors:  David Korczynski and Heng Yin
        Title:  Capturing Malware Propagations with Code Injections and Code-Reuse Attacks
        Normalised: capturingmalwarepropagationswithcodeinjectionsandcodereuseattacks
        -------------------
        Authors:  Christopher Kruegel, Engin Kirda, Darren Mutz, William Robertson, and Gio- vanni Vigna
        Title:  Polymorphic Worm Detection Using Structural Information of Executables
        Normalised: polymorphicwormdetectionusingstructuralinformationofexecutables
        -------------------
        Authors:  Christopher Kruegel, William Robertson, Fredrik Valeur, and Giovanni Vigna
        Title:  Static Disassembly of Obfuscated Binaries
        Normalised: staticdisassemblyofobfuscatedbinaries
        -------------------
        Authors:  Yujia Li, Chenjie Gu, Thomas Dullien, Oriol Vinyals, and Pushmeet Kohli
        Title:  Graph Matching Networks for Learning the Similarity of Graph Structured Objects
        Normalised: graphmatchingnetworksforlearningthesimilarityofgraphstructuredobjects
        -------------------
        Authors:  L. Martignoni, M. Christodorescu, and S. Jha
        Title:  OmniUnpack: Fast, Generic, and Safe Unpacking of Malware
        Normalised: omniunpack:fastgenericandsafeunpackingofmalware
        -------------------
        Authors:  Mario Polino, Andrea Continella, Sebastiano Mariani, Stefano DAlessio, Lorenzo Fontana, Fabio Gritti, and Stefano Zanero
        Title:  Measuring and Defeating Anti- Instrumentation-Equipped Malware
        Normalised: measuringanddefeatingantiinstrumentationequippedmalware
        -------------------
        Authors:  Georgios Portokalidis, Asia Slowinska, and Herbert Bos
        Title:  Argos: an Emula- tor for Fingerprinting Zero-Day Attacks
        Normalised: argos:anemulatorforfingerprintingzerodayattacks
        -------------------
        Authors:  Symantec Security Response
        Title:  W32
        Normalised: w32
        -------------------
        Authors:  Nathan E. Rosenblum, Xiaojin Zhu, Barton P. Miller, and Karen Hunt
        Title:  Learning to Analyze Binary Computer Code
        Normalised: learningtoanalyzebinarycomputercode
        -------------------
        Authors:  Paul Royal, Mitch Halpin, David Dagon, Robert Edmonds, and Wenke Lee
        Title:  PolyUnpack: Automating the Hidden-Code Extraction of Unpack-Executing Malware
        Normalised: polyunpack:automatingthehiddencodeextractionofunpackexecutingmalware
        -------------------
        Authors:  Monirul Sharif, Vinod Yegneswaran, Hassen Saidi, Phillip Porras, and Wenke Lee
        Title:  Eureka: A Framework for Enabling Static Malware Analysis
        Normalised: eureka:aframeworkforenablingstaticmalwareanalysis
        -------------------
        Authors:  Richard L. Sites, Anton Chernoff, Matthew B. Kirk, Maurice P. Marks, and Scott G. Robinson
        Title:  Binary Translation
        Normalised: binarytranslation
        -------------------
        Authors:  Wei Song, Heng Yin, Chang Liu, and Dawn Song
        Title:  DeepMem: Learning Graph Neural Network Models for Fast and Robust Memory Forensic Analysis
        Normalised: deepmem:learninggraphneuralnetworkmodelsforfastandrobustmemoryforensicanalysis
        -------------------
        Authors:  Heng Yin, Dawn Song, Manuel Egele, Christopher Kruegel, and Engin Kirda
        Title:  Panorama: Capturing System-wide Information Flow for Malware De- tection and Analysis
        Normalised: panorama:capturingsystemwideinformationflowformalwaredetectionandanalysis
        -------------------
######################################
Papers in the data set :
Cited papers:
    b'Precise system-wide concatic malware unpacking '
Noncited papers:
    b'A characterisation of system-wide propagation in the malware landscape '
Succ: 2
Fail: 0
Succ sigs: 61
Failed sigs: 2
######################################
All Titles (normalised) of the papers in the data set:
    b'A characterisation of system-wide propagation in the malware landscape '
    b'Precise system-wide concatic malware unpacking '
######################################
######################################
All references/citations (normalised) issued by these papers
    Name : Count
    hostbasedcodeinjectionattacks:apopulartechniqueusedbymalware :  1
    aviewoncurrentmalwarebehaviors :  1
    dynamicanalysisofmaliciouscode :  1
    dridexscoldwar:enteratombombing :  1
    qemuafastandportabledynamictranslator :  1
    asurveyonautomateddynamicmalwareanalysistechniquesandtools :  1
    asurveyofmobilemalwareinthewild :  1
    precisesystemwideconcaticmalwareunpacking :  1
    theevolutionofandroidmalwareandandroidanalysistechniques :  1
    dissectingandroidmalware:characterizationandevolution :  1
    wysinwyx:whatyouseeisnotwhatyouexecute :  1
    byteweight:learningtorecognizefunctionsinbinarycode :  1
    minemu:theworldsfastesttainttracker :  1
    decompilationofbinaryprograms :  1
    ether:malwareanalysisviahardwarevirtualizationextensions :  1
    graphbasedcomparisonofexecutableobjects(englishversion) :  1
    signaturesforlibraryfunctionsinexecutablefiles :  1
    structuralcomparisonofexecutableobjects :  1
    astudyofthepackerproblemanditssolutions :  1
    mutantxs:scalablemalwareclusteringbasedonstaticfeatures :  1
    http://www :  1
    malwash:washingmalwaretoevadedynamicanalysis :  1
    labelinglibraryfunctionsinstrippedbinaries :  1
    secureandadvancedunpackingusingcomputeremulation :  1
    malwaredynamicrecompilation :  1
    taintassistediatreconstructionagainstpositionobfuscation :  1
    thepowerofprocrastination:detectionandmitigationofexecutionstallingmaliciouscode :  1
    polymorphicwormdetectionusingstructuralinformationofexecutables :  1
    staticdisassemblyofobfuscatedbinaries :  1
    graphmatchingnetworksforlearningthesimilarityofgraphstructuredobjects :  1
    omniunpack:fastgenericandsafeunpackingofmalware :  1
    measuringanddefeatingantiinstrumentationequippedmalware :  1
    argos:anemulatorforfingerprintingzerodayattacks :  1
    w32 :  1
    learningtoanalyzebinarycomputercode :  1
    polyunpack:automatingthehiddencodeextractionofunpackexecutingmalware :  1
    eureka:aframeworkforenablingstaticmalwareanalysis :  1
    binarytranslation :  1
    deepmem:learninggraphneuralnetworkmodelsforfastandrobustmemoryforensicanalysis :  1
    systemlevelsupportforintrusionrecovery :  2
    quincy:detectinghostbasedcodeinjectionattacksinmemorydumps :  2
    beemaster:detectinghostbasedcodeinjectionattacks :  2
    codisasm:mediumscaleconcaticdisassemblyofselfmodifyingbinarieswithoverlappinginstructions :  2
    repeatablereverseengineeringwithpanda :  2
    decaf:aplatformneutralwholesystemdynamicbinaryanalysisplatform :  2
    renovo:ahiddencodeextractorforpackedexecutables :  2
    apichaser:taintassistedsandboxforevasivemalwareanalysis :  2
    repeconstruct:reconstructingbinarieswithselfmodifyingcodeandimportaddresstabledestruction :  2
    capturingmalwarepropagationswithcodeinjectionsandcodereuseattacks :  2
    panorama:capturingsystemwideinformationflowformalwaredetectionandanalysis :  2
######################################
The total number of unique citations: 50
######################################
Dependency graph based on citations
Paper:
    pq-out/out-0/json_data/json_dump_0.json
    b'A characterisation of system-wide propagation in the malware landscape '
    Normalised title: acharacterisationofsystemwidepropagationinthemalwarelandscape
    Cited by: 
---------------------------------
Paper:
    pq-out/out-0/json_data/json_dump_1.json
    b'Precise system-wide concatic malware unpacking '
    Normalised title: precisesystemwideconcaticmalwareunpacking
    Cited by: 
        b'A characterisation of system-wide propagation in the malware landscape '
---------------------------------
```
