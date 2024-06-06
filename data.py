# data.py
flashcards = {
    'C#': [
        {'Q': 'What is C#?', 'A': 'C# is a modern, object-oriented programming language developed by Microsoft.'},
        {'Q': 'Explain the concept of inheritance in C#.', 'A': 'Inheritance allows a class to inherit members (fields, methods) from another class.'},
        {'Q': 'What are the different types of classes in C#?', 'A': 'In C#, classes can be static, sealed, abstract, and partial.'},
        {'Q': 'What is the difference between a class and an object in C#?', 'A': 'A class is a blueprint for creating objects. An object is an instance of a class.'},
        {'Q': 'What is the use of the "using" statement in C#?', 'A': 'The "using" statement is used to include the namespaces in the program. It can also be used to ensure that IDisposable objects are disposed of.'},
        {'Q': 'What is a constructor in C#?', 'A': 'A constructor is a special method of a class that initializes objects of that class. It has the same name as the class and does not have a return type.'},
        {'Q': 'Explain the concept of polymorphism in C#.', 'A': 'Polymorphism allows methods to have the same name but behave differently based on the object that is calling them. It is achieved through method overloading and method overriding.'},
        {'Q': 'What is the difference between method overloading and method overriding in C#?', 'A': 'Method overloading allows multiple methods to have the same name but different parameters. Method overriding allows a subclass to provide a specific implementation for a method that is already defined in its superclass.'},
        {'Q': 'What is the purpose of the "virtual" keyword in C#?', 'A': 'The "virtual" keyword is used to declare a method or property that can be overridden in derived classes.'},
        {'Q': 'What is the difference between "ref" and "out" parameters in C#?', 'A': 'Both "ref" and "out" are used to pass arguments by reference. The "ref" keyword requires that the parameter be initialized before it is passed, while the "out" keyword does not.'},
        {'Q': 'What is a delegate in C#?', 'A': 'A delegate is a type that represents references to methods with a particular parameter list and return type. Delegates are used to pass methods as arguments to other methods.'},
        {'Q': 'What is an event in C#?', 'A': 'An event is a message sent by an object to signal the occurrence of an action. Events are typically used in graphical user interfaces and other asynchronous applications.'},
        {'Q': 'What is the purpose of the "static" keyword in C#?', 'A': 'The "static" keyword is used to declare members that belong to the type itself rather than to any specific object. Static members are shared by all instances of the class.'},
        {'Q': 'What is exception handling in C#?', 'A': 'Exception handling in C# is a way to handle runtime errors using try, catch, and finally blocks. It allows a program to continue executing after an error has been handled.'},
        {'Q': 'What are generics in C#?', 'A': 'Generics allow you to define classes, methods, and data structures with a placeholder for the type of data they store or use. This allows for type-safe and reusable code.'},
        {'Q': 'What is LINQ in C#?', 'A': 'LINQ (Language Integrated Query) is a set of features that adds query capabilities to the C# language. It allows querying of arrays, collections, databases, and more using a consistent syntax.'},
        {'Q': 'What is the difference between "==" and "Equals" in C#?', 'A': 'The "==" operator compares the reference identity (for reference types) or value (for value types). The "Equals" method compares the value equality of objects.'},
        {'Q': 'What is the purpose of the "async" and "await" keywords in C#?', 'A': 'The "async" keyword is used to declare a method that contains asynchronous operations. The "await" keyword is used to pause the execution of an async method until the awaited task completes.'},
        {'Q': 'What is the purpose of the "sealed" keyword in C#?', 'A': 'The "sealed" keyword is used to prevent a class from being inherited or a method from being overridden.'},
        {'Q': 'What are extension methods in C#?', 'A': 'Extension methods allow you to add new methods to existing types without modifying the original type. They are defined as static methods in a static class.'},
        {'Q': 'What is a nullable type in C#?', 'A': 'A nullable type is a value type that can also represent null. It is declared using the "?" symbol (e.g., int? or bool?).'},
        {'Q': 'What is the difference between an interface and an abstract class in C#?', 'A': 'An interface only contains declarations of methods, properties, events, or indexers. An abstract class can include implementations of methods and fields, as well as declarations.'},
        {'Q': 'What is the purpose of the "lock" statement in C#?', 'A': 'The "lock" statement is used to ensure that a block of code runs to completion without being interrupted by other threads, providing thread safety.'},
        {'Q': 'What is the difference between "public", "private", "protected", and "internal" access modifiers in C#?', 'A': '"Public" allows access from any code. "Private" restricts access to the containing class. "Protected" allows access to the containing class and derived classes. "Internal" allows access within the same assembly.'},
        # C# Basics: Syntax and Structure
        {'Q': 'What are the basic data types in C#?', 'A': 'Basic data types in C# include int, float, double, char, string, bool, and decimal.'},
        {'Q': 'How do you declare a variable in C#?', 'A': 'A variable in C# is declared with a type followed by a name, e.g., int myVariable;'},
        {'Q': 'What are constants and how do you define them in C#?', 'A': 'Constants are immutable values defined using the "const" keyword, e.g., const int myConstant = 10;'},
        {'Q': 'What are the different types of operators in C#?', 'A': 'C# operators include arithmetic (e.g., +, -, *, /), relational (e.g., ==, !=, >, <), logical (e.g., &&, ||, !), and bitwise (e.g., &, |, ^, ~) operators.'},
        # Control Flow
        {'Q': 'What are conditional statements in C#?', 'A': 'Conditional statements include if, else if, else, and switch. They are used to execute code based on certain conditions.'},
        {'Q': 'Describe the different types of loops in C#.', 'A': 'C# supports for, while, do-while, and foreach loops for iterating over collections or performing repetitive tasks.'},
        # Arrays and Collections
        {'Q': 'How do you declare and initialize a one-dimensional array in C#?', 'A': 'A one-dimensional array is declared and initialized as follows: int[] myArray = new int[5];'},
        {'Q': 'What are collections in C# and name some common types?', 'A': 'Collections in C# are dynamic data structures. Common types include List, Dictionary, Queue, and Stack.'},
        # Object-Oriented Programming (OOP): Classes and Objects
        {'Q': 'What are properties in C#?', 'A': 'Properties are members that provide a flexible mechanism to read, write, or compute the value of a private field. They use get and set accessors.'},
        {'Q': 'What is the purpose of a constructor in C#?', 'A': 'Constructors are special methods used to initialize objects. They are called when an instance of a class is created.'},
        # Inheritance
        {'Q': 'What is a base class and a derived class in C#?', 'A': 'A base class provides basic functionality, while a derived class inherits from the base class and can add or override members.'},
        # Polymorphism
        {'Q': 'Explain method overloading in C#.', 'A': 'Method overloading allows multiple methods in the same class to have the same name but different parameters.'},
        {'Q': 'What is method overriding in C#?', 'A': 'Method overriding allows a derived class to provide a specific implementation of a method that is already defined in its base class.'},
        # Encapsulation
        {'Q': 'What are access modifiers in C#?', 'A': 'Access modifiers control the accessibility of classes and members. Common modifiers include public, private, protected, and internal.'},
        # Abstraction
        {'Q': 'What is an abstract class in C#?', 'A': 'An abstract class cannot be instantiated and may contain abstract methods, which must be implemented by derived classes.'},
        {'Q': 'What is an interface in C#?', 'A': 'An interface defines a contract that classes can implement. It contains method declarations but no implementations.'},
        # Advanced C# Concepts: Delegates and Events
        {'Q': 'What is a delegate in C#?', 'A': 'A delegate is a type-safe function pointer that can reference methods with a specific signature.'},
        {'Q': 'How do you declare and use events in C#?', 'A': 'Events are declared using the event keyword and are used to notify subscribers when something happens. Example: public event EventHandler MyEvent;'},
        # LINQ (Language Integrated Query)
        {'Q': 'What is LINQ in C#?', 'A': 'LINQ (Language Integrated Query) provides a consistent way to query various data sources, like arrays, collections, and databases.'},
        {'Q': 'Give an example of a basic LINQ query in C#.', 'A': 'A basic LINQ query: var result = from s in myArray where s.Length > 3 select s;'},
        # Exception Handling
        {'Q': 'What is a try-catch block in C#?', 'A': 'A try-catch block is used to handle exceptions. Code that may throw an exception is placed in the try block, and exception handling code is in the catch block.'},
        {'Q': 'How do you create custom exceptions in C#?', 'A': 'Custom exceptions are created by inheriting from the Exception class, e.g., public class MyCustomException : Exception {}'},
        # Asynchronous Programming
        {'Q': 'What are async and await keywords in C#?', 'A': 'The async keyword is used to define an asynchronous method, and await is used to pause the execution until the awaited task completes.'},
        # Reflection
        {'Q': 'What is reflection in C#?', 'A': 'Reflection is the ability to inspect metadata and assemblies at runtime. It is used to dynamically create instances of types, bind to methods, and retrieve information about types.'},
        # File I/O
        {'Q': 'How do you read a file in C#?', 'A': 'Files are read using the System.IO namespace. Example: string text = File.ReadAllText("file.txt");'},
        {'Q': 'How do you write to a file in C#?', 'A': 'Files are written using the System.IO namespace. Example: File.WriteAllText("file.txt", "Hello, World!");'}
    ],
    '.NET': [
        # .NET Basics
        {'Q': 'What is .NET?', 'A': '.NET is a free, cross-platform, open-source developer platform for building many different types of applications.'},
        {'Q': 'What are the main components of the .NET framework?', 'A': 'The main components are the Common Language Runtime (CLR), the .NET Framework Class Library (FCL), and ASP.NET for web development.'},
        {'Q': 'What is the CLR in .NET?', 'A': 'The Common Language Runtime (CLR) is the virtual machine component of the .NET framework that manages the execution of .NET programs.'},
        {'Q': 'What is the .NET Framework Class Library (FCL)?', 'A': 'The FCL is a comprehensive collection of reusable types, including classes, interfaces, and value types, that are tightly integrated with the CLR.'},
        
        # ASP.NET
        {'Q': 'What is ASP.NET?', 'A': 'ASP.NET is an open-source server-side web application framework designed for web development to produce dynamic web pages.'},
        {'Q': 'What are Web Forms in ASP.NET?', 'A': 'Web Forms are a part of the ASP.NET web application framework and are one of the three programming models you can use to create ASP.NET web applications.'},
        {'Q': 'What is MVC in ASP.NET?', 'A': 'MVC stands for Model-View-Controller. It is a pattern used for creating web applications where the application is divided into three main components: Model, View, and Controller.'},
        
        # .NET Core
        {'Q': 'What is .NET Core?', 'A': '.NET Core is a free, cross-platform, open-source developer platform for building many different types of applications. It is the successor to the .NET Framework.'},
        {'Q': 'What are the advantages of using .NET Core?', 'A': '.NET Core is cross-platform, high performance, supports modern application development, and is open-source.'},
        {'Q': 'What is the difference between .NET Framework and .NET Core?', 'A': '.NET Framework is used for building Windows applications, while .NET Core is cross-platform and used for building applications that run on Windows, macOS, and Linux.'},
        
        # Entity Framework
        {'Q': 'What is Entity Framework?', 'A': 'Entity Framework (EF) is an open-source object-relational mapper (ORM) framework for ADO.NET, which allows developers to work with a database using .NET objects.'},
        {'Q': 'What are the different types of Entity Framework workflows?', 'A': 'The different types are Database-First, Model-First, and Code-First workflows.'},
        {'Q': 'What is Code-First approach in Entity Framework?', 'A': 'In the Code-First approach, you define your model using C# or VB.NET classes. The database schema is created based on the model classes.'},
        
        # Web API
        {'Q': 'What is a Web API?', 'A': 'A Web API is an application programming interface for either a web server or a web browser. It is a framework that makes it easy to build HTTP services that reach a broad range of clients, including browsers and mobile devices.'},
        {'Q': 'What is the difference between WCF and Web API?', 'A': 'WCF is used for building service-oriented applications, while Web API is used for building RESTful services.'},
        {'Q': 'How do you secure a Web API?', 'A': 'You can secure a Web API using authentication and authorization mechanisms such as OAuth, JWT, and API keys.'},
        
        # LINQ (Language Integrated Query)
        {'Q': 'What is LINQ?', 'A': 'LINQ (Language Integrated Query) is a set of features that adds query capabilities to the .NET language syntax. It allows querying of arrays, collections, databases, and more using a consistent syntax.'},
        {'Q': 'What are the different types of LINQ?', 'A': 'The different types of LINQ include LINQ to Objects, LINQ to XML, LINQ to SQL, and LINQ to Entities.'},
        {'Q': 'Give an example of a basic LINQ query.', 'A': 'Example: var result = from s in myArray where s.Length > 3 select s;'},
        
        # Exception Handling
        {'Q': 'How do you handle exceptions in .NET?', 'A': 'Exceptions are handled using try, catch, and finally blocks. You can also create custom exceptions by inheriting from the Exception class.'},
        {'Q': 'What is a custom exception?', 'A': 'A custom exception is a user-defined exception that is derived from the Exception class. It is used to handle application-specific errors.'},
        
        # Asynchronous Programming
        {'Q': 'What are async and await in .NET?', 'A': 'The async keyword is used to declare an asynchronous method, and await is used to pause the execution until the awaited task completes.'},
        {'Q': 'What is the purpose of Task in .NET?', 'A': 'Task represents an asynchronous operation and is part of the Task Parallel Library (TPL). It provides a way to handle asynchronous code in a more manageable way.'},
        
        # Reflection
        {'Q': 'What is reflection in .NET?', 'A': 'Reflection is the ability to inspect metadata and assemblies at runtime. It is used to dynamically create instances of types, bind to methods, and retrieve information about types.'},
        {'Q': 'Give an example of using reflection in .NET.', 'A': 'Example: Type type = typeof(MyClass); MethodInfo method = type.GetMethod("MyMethod"); object result = method.Invoke(instance, parameters);'},
        
        # Dependency Injection
        {'Q': 'What is Dependency Injection in .NET?', 'A': 'Dependency Injection (DI) is a design pattern used to implement IoC, where the control of creating and binding the dependent objects is moved out of the class that depends on them.'},
        {'Q': 'What are the benefits of using Dependency Injection?', 'A': 'Benefits include improved code maintainability, testability, and decoupling of components.'},
        {'Q': 'What are the types of Dependency Injection?', 'A': 'The types of Dependency Injection are Constructor Injection, Property Injection, and Method Injection.'},
        
        # Microservices
        {'Q': 'What are microservices?', 'A': 'Microservices are an architectural style that structures an application as a collection of small, autonomous services modeled around a business domain.'},
        {'Q': 'What are the benefits of using microservices?', 'A': 'Benefits include improved scalability, flexibility, and the ability to develop and deploy services independently.'},
        {'Q': 'How do you implement microservices in .NET?', 'A': 'Microservices in .NET can be implemented using .NET Core and technologies like Docker, Kubernetes, and Azure Service Fabric.'},
        
        # .NET Security
        {'Q': 'What are some common security practices in .NET?', 'A': 'Common practices include using HTTPS, validating input, using authentication and authorization, and keeping dependencies updated.'},
        {'Q': 'How do you implement authentication in ASP.NET Core?', 'A': 'Authentication in ASP.NET Core can be implemented using middleware like ASP.NET Core Identity, JWT, and OAuth.'},
        {'Q': 'What is data encryption and how is it implemented in .NET?', 'A': 'Data encryption converts data into a coded form to prevent unauthorized access. In .NET, it can be implemented using classes from the System.Security.Cryptography namespace.'},
        
        # Performance Optimization
        {'Q': 'How do you improve performance in a .NET application?', 'A': 'Performance can be improved by optimizing code, using caching, minimizing I/O operations, and utilizing asynchronous programming.'},
        {'Q': 'What is caching and how is it implemented in .NET?', 'A': 'Caching is the process of storing frequently accessed data in memory to improve performance. It can be implemented using MemoryCache or distributed caching solutions like Redis.'},
        # .NET Framework: Architecture and Components
        {'Q': 'What is the architecture of the .NET Framework?', 'A': 'The .NET Framework architecture consists of the Common Language Runtime (CLR), the Framework Class Library (FCL), ASP.NET for web applications, Windows Forms for desktop applications, and ADO.NET for data access.'},

        # Common Language Runtime (CLR)
        {'Q': 'What is the Common Language Runtime (CLR)?', 'A': 'The CLR is the virtual machine component of the .NET Framework that manages the execution of .NET programs. It provides services such as memory management, security, and exception handling.'},

        # Framework Class Library (FCL)
        {'Q': 'What is the Framework Class Library (FCL)?', 'A': 'The FCL is a comprehensive collection of reusable classes, interfaces, and value types that are tightly integrated with the CLR. It provides a consistent, object-oriented programming environment for developers.'},

        # Memory Management: Garbage Collection
        {'Q': 'What is garbage collection in .NET?', 'A': 'Garbage collection in .NET is an automatic memory management feature that reclaims memory occupied by objects that are no longer in use. It helps to avoid memory leaks and optimize memory usage.'},

        # Assemblies: DLLs and EXEs
        {'Q': 'What is an assembly in .NET?', 'A': 'An assembly is a compiled code library used for deployment, versioning, and security in .NET applications. It can be a DLL (Dynamic Link Library) or an EXE (Executable) file.'},
        {'Q': 'What is the difference between a DLL and an EXE in .NET?', 'A': 'A DLL (Dynamic Link Library) is a library that contains code and data that can be used by multiple programs simultaneously. An EXE (Executable) file is an application that can be run standalone.'},

        # GAC (Global Assembly Cache)
        {'Q': 'What is the Global Assembly Cache (GAC)?', 'A': 'The GAC is a machine-wide code cache that stores assemblies specifically designated to be shared by several applications on the computer. It allows multiple versions of the same assembly to be stored and managed.'},

        # Versioning and Deployment
        {'Q': 'How does versioning work in .NET?', 'A': 'Versioning in .NET involves specifying version numbers for assemblies. The CLR can load different versions of the same assembly side by side. Version numbers consist of major, minor, build, and revision numbers.'},
        {'Q': 'What are the deployment options for .NET applications?', 'A': 'Deployment options for .NET applications include XCOPY deployment, Windows Installer, ClickOnce deployment, and more recently, containerization with Docker.'},

        # .NET Core: .NET Core vs .NET Framework
        {'Q': 'What is the difference between .NET Core and .NET Framework?', 'A': '.NET Framework is used for building Windows applications and is not cross-platform, while .NET Core is cross-platform and can be used for building applications that run on Windows, macOS, and Linux.'},

        # Cross-Platform Development
        {'Q': 'How does .NET Core support cross-platform development?', 'A': '.NET Core supports cross-platform development by being built on an open-source runtime that can run on multiple operating systems including Windows, macOS, and Linux.'},

        # Project Structure
        {'Q': 'What is the typical project structure of a .NET Core application?', 'A': 'A typical .NET Core project structure includes folders for Properties, wwwroot, Controllers, Models, Views, and a project file (.csproj) that contains metadata about the project and dependencies.'},

        # Package Management with NuGet
        {'Q': 'What is NuGet in .NET?', 'A': 'NuGet is a package manager for .NET. It allows developers to create, share, and consume useful .NET libraries. NuGet packages are hosted on nuget.org, and they can be installed via the NuGet Package Manager in Visual Studio.'},

        # ASP.NET Core: MVC Architecture
        {'Q': 'What is MVC in ASP.NET Core?', 'A': 'MVC stands for Model-View-Controller. It is a design pattern used for developing web applications. The Model represents the application data, the View displays the data, and the Controller handles the input and interactions.'},
        {'Q': 'What are Models in ASP.NET Core MVC?', 'A': 'Models in ASP.NET Core MVC are classes that represent the data of the application. They are used to pass data between the Controller and the View.'},
        {'Q': 'What are Views in ASP.NET Core MVC?', 'A': 'Views in ASP.NET Core MVC are the components that display the application’s user interface. They use Razor syntax to embed server-based code into HTML.'},
        {'Q': 'What are Controllers in ASP.NET Core MVC?', 'A': 'Controllers in ASP.NET Core MVC handle the user input, work with the Model, and select a View to render that displays the user interface.'},

        # Razor Pages
        {'Q': 'What are Razor Pages in ASP.NET Core?', 'A': 'Razor Pages are a simplified programming model for building web UI in ASP.NET Core. Each Razor Page is self-contained with its view and code separated into a single file with .cshtml extension.'},
        {'Q': 'How do you use Razor syntax in ASP.NET Core?', 'A': 'Razor syntax is used to embed C# code in HTML. It uses the @ symbol to switch from HTML to C# and can include variables, loops, and conditionals.'},

        # RESTful APIs
        {'Q': 'How do you create a RESTful API in ASP.NET Core?', 'A': 'To create a RESTful API in ASP.NET Core, you define a controller with [ApiController] attribute and define actions that respond to HTTP requests. The [HttpGet], [HttpPost], [HttpPut], and [HttpDelete] attributes are used to map HTTP verbs to controller methods.'},
        {'Q': 'How do you consume a RESTful API in ASP.NET Core?', 'A': 'A RESTful API can be consumed using HttpClient, a class in the System.Net.Http namespace that sends HTTP requests and receives HTTP responses from a resource identified by a URI.'},
        {'Q': 'What is Swagger and how is it used for API documentation in ASP.NET Core?', 'A': 'Swagger is an open-source framework for API documentation. In ASP.NET Core, it is used to generate interactive API documentation and includes tools for auto-generating documentation from API code using the Swashbuckle package.'},

        # Dependency Injection
        {'Q': 'What is Dependency Injection (DI) in ASP.NET Core?', 'A': 'Dependency Injection is a design pattern used in ASP.NET Core to achieve Inversion of Control (IoC) between classes and their dependencies. ASP.NET Core provides a built-in DI container to manage object lifetimes and dependencies.'},

        # Middleware
        {'Q': 'What is middleware in ASP.NET Core?', 'A': 'Middleware is software that is assembled into an application pipeline to handle requests and responses. Each component chooses whether to pass the request to the next component in the pipeline or to handle the request itself.'},
        {'Q': 'How do you create custom middleware in ASP.NET Core?', 'A': 'Custom middleware in ASP.NET Core is created by defining a class with an Invoke or InvokeAsync method. This class is then added to the application pipeline in the Configure method of the Startup class using the app.UseMiddleware<>() method.'},

        # Entity Framework Core
        {'Q': 'What is Entity Framework Core?', 'A': 'Entity Framework Core (EF Core) is a lightweight, extensible, open-source, and cross-platform version of the popular Entity Framework data access technology. It allows developers to work with a database using .NET objects.'},
        {'Q': 'What is the Code First approach in Entity Framework Core?', 'A': 'In the Code First approach, you define your database schema through C# or VB.NET classes. The database is then created based on these classes using migrations.'},
        {'Q': 'What is the Database First approach in Entity Framework Core?', 'A': 'In the Database First approach, you create the database first, and then generate the entity classes and context from the existing database schema.'},
        {'Q': 'How do you use LINQ with Entity Framework Core?', 'A': 'LINQ (Language Integrated Query) can be used with EF Core to write queries against the database in a strongly-typed manner. Example: var users = context.Users.Where(u => u.IsActive).ToList();'}
    ],
    'Angular': [
        # Angular Basics
        {'Q': 'What is Angular?', 'A': 'Angular is a platform and framework for building single-page client applications using HTML and TypeScript.'},
        {'Q': 'What are the key features of Angular?', 'A': 'Key features of Angular include a component-based architecture, two-way data binding, dependency injection, directives, services, and a powerful CLI.'},

        # Angular Architecture
        {'Q': 'What is the architecture of an Angular application?', 'A': 'The architecture of an Angular application consists of modules, components, templates, metadata, data binding, directives, services, and dependency injection.'},
        {'Q': 'What is a module in Angular?', 'A': 'A module in Angular is a container for a cohesive block of code dedicated to an application domain, a workflow, or a set of related capabilities. It is defined using the @NgModule decorator.'},

        # Components
        {'Q': 'What is a component in Angular?', 'A': 'A component is a building block of Angular applications. It controls a patch of the screen called a view. Components are defined using the @Component decorator.'},
        {'Q': 'How do you create a component in Angular?', 'A': 'A component is created using the Angular CLI with the command `ng generate component component-name`. It includes a TypeScript class, an HTML template, and a CSS style file.'},

        # Templates
        {'Q': 'What is a template in Angular?', 'A': 'A template in Angular is a part of a component that defines the view. It contains HTML, along with Angular-specific syntax for binding and directives.'},
        {'Q': 'What is interpolation in Angular?', 'A': 'Interpolation is a data binding technique that allows you to embed expressions within double curly braces {{ }} to display dynamic data in the template.'},

        # Data Binding
        {'Q': 'What are the different types of data binding in Angular?', 'A': 'The different types of data binding in Angular are: Interpolation, Property binding, Event binding, and Two-way binding.'},
        {'Q': 'What is two-way data binding in Angular?', 'A': 'Two-way data binding allows for the synchronization of data between the model and the view. It is implemented using the ngModel directive.'},

        # Directives
        {'Q': 'What are directives in Angular?', 'A': 'Directives are classes that add behavior to elements in Angular applications. There are three types of directives: component directives, structural directives (e.g., *ngIf, *ngFor), and attribute directives (e.g., ngClass, ngStyle).'},
        {'Q': 'What is the difference between a structural directive and an attribute directive?', 'A': 'Structural directives change the DOM layout by adding or removing elements (e.g., *ngIf, *ngFor), whereas attribute directives change the appearance or behavior of an element without altering the DOM structure (e.g., ngClass, ngStyle).'},

        # Services and Dependency Injection
        {'Q': 'What are services in Angular?', 'A': 'Services are singleton objects that carry out specific tasks and can be shared across components. They are typically used for data sharing, business logic, and external interactions like HTTP requests.'},
        {'Q': 'What is dependency injection in Angular?', 'A': 'Dependency Injection (DI) is a design pattern used in Angular to manage and inject dependencies into components and services. It helps to create more modular and testable code.'},

        # Angular Router
        {'Q': 'What is the Angular Router?', 'A': 'The Angular Router is a module that provides navigation and URL manipulation capabilities in Angular applications. It allows developers to define routes and navigate between views.'},
        {'Q': 'How do you configure routes in Angular?', 'A': 'Routes are configured in Angular using the RouterModule.forRoot() method, which defines an array of routes, each mapping a URL path to a component.'},

        # Forms
        {'Q': 'What are the different types of forms in Angular?', 'A': 'Angular supports two types of forms: Template-driven forms and Reactive forms. Template-driven forms are based on directives in the template, while reactive forms are created programmatically using form control objects.'},
        {'Q': 'How do you handle form validation in Angular?', 'A': 'Form validation in Angular can be handled using built-in validators (e.g., required, minlength, maxlength) or custom validators. Validators are applied to form controls to check for specific conditions.'},

        # HTTP Client
        {'Q': 'What is HttpClient in Angular?', 'A': 'HttpClient is a service in Angular that provides an HTTP client API for making HTTP requests to a backend server. It is part of the @angular/common/http module.'},
        {'Q': 'How do you make an HTTP GET request in Angular?', 'A': 'An HTTP GET request is made using the HttpClient.get() method. Example: `this.http.get(url).subscribe(data => { console.log(data); });`'},

        # Angular CLI
        {'Q': 'What is the Angular CLI?', 'A': 'The Angular CLI (Command Line Interface) is a tool that helps to automate the development workflow. It provides commands for creating, building, testing, and deploying Angular applications.'},
        {'Q': 'How do you create a new Angular project using the CLI?', 'A': 'A new Angular project is created using the command `ng new project-name`. The CLI sets up the project structure and installs the necessary dependencies.'},

        # Testing
        {'Q': 'How do you test Angular applications?', 'A': 'Angular applications can be tested using tools like Jasmine for unit testing, Karma as a test runner, and Protractor for end-to-end testing. The Angular CLI provides built-in support for these tools.'},
        {'Q': 'What is a test bed in Angular testing?', 'A': 'A test bed is an Angular testing utility that allows you to create a testing module configuration, which emulates an Angular module. It is used to set up the environment for unit testing components and services.'},

        # Advanced Topics
        {'Q': 'What are Angular modules (NgModules)?', 'A': 'NgModules are containers for a cohesive block of code dedicated to an application domain, a workflow, or a set of related capabilities. They help to organize an application into cohesive blocks of functionality.'},
        {'Q': 'What is lazy loading in Angular?', 'A': 'Lazy loading is a technique in Angular used to load modules asynchronously when a specific route is activated. This helps to improve the application’s performance by loading only the necessary code.'},
        {'Q': 'What is Angular Universal?', 'A': 'Angular Universal is a technology that allows you to run Angular applications on the server, enabling server-side rendering (SSR). It improves performance and SEO by pre-rendering pages on the server.'},
        # Setting up the Environment: Node.js and npm
        {'Q': 'What is Node.js and why is it important for Angular?', 'A': 'Node.js is a JavaScript runtime built on Chrome\'s V8 JavaScript engine. It is important for Angular as it provides the npm package manager, which is used to install Angular CLI and other dependencies.'},
        {'Q': 'What is npm and how is it used in Angular?', 'A': 'npm (Node Package Manager) is a package manager for JavaScript. It is used in Angular to install and manage packages and dependencies required for Angular development.'},

        # Setting up the Environment: Angular CLI
        {'Q': 'What is Angular CLI?', 'A': 'Angular CLI is a command-line interface tool that helps to initialize, develop, scaffold, and maintain Angular applications. It simplifies the development process by providing commands for creating components, services, modules, and more.'},
        {'Q': 'How do you install Angular CLI?', 'A': 'Angular CLI can be installed using npm with the command: npm install -g @angular/cli.'},
        {'Q': 'How do you create a new Angular project using Angular CLI?', 'A': 'A new Angular project can be created using the command: ng new project-name. This sets up the project structure and installs the necessary dependencies.'},

        # Angular Project Structure: Modules, Components, Templates
        {'Q': 'What is the typical project structure of an Angular application?', 'A': 'The typical project structure includes folders such as src (source files), app (application modules, components, and services), assets (static assets), environments (environment-specific configurations), and the angular.json file for project configuration.'},
        {'Q': 'What is an Angular module?', 'A': 'An Angular module is a container for a cohesive block of code dedicated to an application domain, a workflow, or a set of related capabilities. It is defined using the @NgModule decorator and can contain components, services, directives, and pipes.'},
        {'Q': 'What is a component in Angular?', 'A': 'A component is a fundamental building block of Angular applications. It controls a patch of the screen called a view and is defined using the @Component decorator.'},
        {'Q': 'What is a template in Angular?', 'A': 'A template in Angular is part of a component that defines the view. It contains HTML along with Angular-specific syntax for binding and directives.'},

        # Data Binding: Interpolation
        {'Q': 'What is interpolation in Angular?', 'A': 'Interpolation is a data binding technique that allows you to embed expressions within double curly braces {{ }} to display dynamic data in the template.'},

        # Data Binding: Property Binding
        {'Q': 'What is property binding in Angular?', 'A': 'Property binding is a technique that binds a property of a DOM element to a property in the component. It is done using square brackets [] around the property name, e.g., [src]="imageUrl".'},

        # Data Binding: Event Binding
        {'Q': 'What is event binding in Angular?', 'A': 'Event binding is a technique that binds a DOM event to a method in the component. It is done using parentheses () around the event name, e.g., (click)="onClick()".'},

        # Data Binding: Two-way Binding
        {'Q': 'What is two-way data binding in Angular?', 'A': 'Two-way data binding allows for the synchronization of data between the model and the view. It is implemented using the ngModel directive and the [( )] syntax, e.g., [(ngModel)]="data".'},

        # Angular Components: Component Lifecycle Hooks
        {'Q': 'What are Angular component lifecycle hooks?', 'A': 'Lifecycle hooks are methods that provide visibility into key moments in a component\'s life. They include ngOnInit, ngOnChanges, ngDoCheck, ngAfterContentInit, ngAfterContentChecked, ngAfterViewInit, ngAfterViewChecked, and ngOnDestroy.'},

        # Angular Components: Component Communication
        {'Q': 'How do components communicate with each other in Angular?', 'A': 'Components communicate with each other using @Input() and @Output() decorators. @Input() is used to pass data from a parent component to a child component, and @Output() is used to emit events from a child component to a parent component.'},

        # Angular Components: Directives
        {'Q': 'What are structural directives in Angular?', 'A': 'Structural directives are directives that change the DOM layout by adding or removing elements. Common structural directives include *ngIf for conditionally including an element, and *ngFor for repeating an element for each item in a collection.'},
        {'Q': 'What are attribute directives in Angular?', 'A': 'Attribute directives change the appearance or behavior of an element without altering the DOM structure. Common attribute directives include ngClass for adding/removing classes and ngStyle for applying styles.'},

        # Services and Dependency Injection: Creating and using services
        {'Q': 'What are services in Angular?', 'A': 'Services are singleton objects that encapsulate logic and data that can be shared across components. They are typically used for data sharing, business logic, and interacting with external APIs.'},
        {'Q': 'How do you create a service in Angular?', 'A': 'A service is created using the Angular CLI with the command: ng generate service service-name. It generates a TypeScript class decorated with @Injectable().'},

        # Services and Dependency Injection: Dependency Injection
        {'Q': 'What is dependency injection in Angular?', 'A': 'Dependency Injection (DI) is a design pattern used in Angular to manage and inject dependencies into components and services. It helps to create more modular, testable, and maintainable code.'},

        # Routing and Navigation: Router Module
        {'Q': 'What is the Angular Router?', 'A': 'The Angular Router is a module that provides navigation and URL manipulation capabilities in Angular applications. It allows developers to define routes and navigate between views.'},
        {'Q': 'How do you configure routes in Angular?', 'A': 'Routes are configured using the RouterModule.forRoot() method, which defines an array of routes, each mapping a URL path to a component. This configuration is typically done in a routing module.'},
        {'Q': 'What are route guards in Angular?', 'A': 'Route guards are services that control navigation to and from routes. They implement interfaces like CanActivate, CanActivateChild, CanDeactivate, CanLoad, and CanMatch to guard routes based on specific conditions.'},
        {'Q': 'What is lazy loading in Angular?', 'A': 'Lazy loading is a technique in Angular used to load modules asynchronously when a specific route is activated. This helps to improve the application’s performance by loading only the necessary code.'},

        # HTTP Client: Making HTTP Requests
        {'Q': 'What is HttpClient in Angular?', 'A': 'HttpClient is a service in Angular that provides an HTTP client API for making HTTP requests to a backend server. It is part of the @angular/common/http module.'},
        {'Q': 'How do you make an HTTP GET request in Angular?', 'A': 'An HTTP GET request is made using the HttpClient.get() method. Example: `this.http.get(url).subscribe(data => { console.log(data); });`'},
        {'Q': 'How do you make an HTTP POST request in Angular?', 'A': 'An HTTP POST request is made using the HttpClient.post() method. Example: `this.http.post(url, body).subscribe(response => { console.log(response); });`'},
        {'Q': 'How do you make an HTTP PUT request in Angular?', 'A': 'An HTTP PUT request is made using the HttpClient.put() method. Example: `this.http.put(url, body).subscribe(response => { console.log(response); });`'},
        {'Q': 'How do you make an HTTP DELETE request in Angular?', 'A': 'An HTTP DELETE request is made using the HttpClient.delete() method. Example: `this.http.delete(url).subscribe(response => { console.log(response); });`'},

        # HTTP Client: Handling Observables with RxJS
        {'Q': 'What is RxJS in Angular?', 'A': 'RxJS (Reactive Extensions for JavaScript) is a library for composing asynchronous and event-based programs using observable sequences. It is used in Angular for handling asynchronous operations like HTTP requests.'},
        {'Q': 'What is an Observable in Angular?', 'A': 'An Observable is a data type that represents a stream of data or events that can be subscribed to. It is a core part of RxJS and is used extensively in Angular for handling asynchronous operations.'},

        # Forms in Angular: Template-Driven Forms
        {'Q': 'What are template-driven forms in Angular?', 'A': 'Template-driven forms rely on Angular directives to build forms directly in the template. They are simple to use and suitable for simple forms. Directives like ngModel are used for two-way data binding.'},

        # Forms in Angular: Reactive Forms
        {'Q': 'What are reactive forms in Angular?', 'A': 'Reactive forms are built using explicit and immutable data structures for the form model in the component class. They provide more control and flexibility over form validation and state.'},
        {'Q': 'What is FormControl in Angular?', 'A': 'FormControl is a class used in reactive forms to represent a single input field. It tracks the value and validation status of the form control.'},
        {'Q': 'What is FormGroup in Angular?', 'A': 'FormGroup is a class used in reactive forms to group related FormControls together. It tracks the value and validation status of the group of controls.'},
        {'Q': 'How do you perform form validation in Angular?', 'A': 'Form validation in Angular can be done using built-in validators (e.g., required, minlength, maxlength) or custom validators. Validators are applied to FormControl and FormGroup instances.'},

        # Advanced Angular Topics: State Management with NgRx
        {'Q': 'What is NgRx in Angular?', 'A': 'NgRx is a set of reactive extensions for Angular, including a state management library that provides a way to manage the state of the application using a single, immutable data store.'},

        # Advanced Angular Topics: Angular Animations
        {'Q': 'How do you implement animations in Angular?', 'A': 'Animations in Angular are implemented using the Angular animations module, which provides a way to define and apply animations using the @angular/animations package and the trigger, state, style, animate, and transition functions.'},

        # Advanced Angular Topics: Internationalization (i18n)
        {'Q': 'What is internationalization (i18n) in Angular?', 'A': 'Internationalization (i18n) in Angular refers to the process of designing and preparing an application to be usable in different languages and locales. Angular provides built-in support for i18n using the Angular CLI and the @angular/localize package.'},

        # Advanced Angular Topics: Performance Optimization
        {'Q': 'How do you optimize the performance of an Angular application?', 'A': 'Performance optimization in Angular can be achieved through various techniques such as lazy loading modules, using the OnPush change detection strategy, optimizing template expressions, and minimizing the bundle size using Angular CLI’s build optimizations.'}
    ],
    'Agile': [
        # Agile Principles and Manifesto
        {'Q': 'What are the Agile principles?', 'A': 'The Agile principles are a set of 12 principles that guide Agile methodologies. They emphasize customer satisfaction, welcoming change, delivering working software frequently, collaboration, motivated individuals, face-to-face communication, working software as a measure of progress, sustainable development, technical excellence, simplicity, self-organizing teams, and regular reflection and adjustment.'},
        {'Q': 'What is the Agile Manifesto?', 'A': 'The Agile Manifesto is a declaration of four foundational values and twelve principles to guide iterative and incremental software development. The values are: Individuals and interactions over processes and tools, Working software over comprehensive documentation, Customer collaboration over contract negotiation, and Responding to change over following a plan.'},

        # Scrum Framework: Roles
        {'Q': 'What are the roles in a Scrum team?', 'A': 'The roles in a Scrum team are the Product Owner, Scrum Master, and Development Team. The Product Owner is responsible for defining the features of the product and prioritizing the backlog. The Scrum Master ensures that the team adheres to Scrum practices and removes impediments. The Development Team is responsible for delivering potentially shippable product increments at the end of each Sprint.'},
        {'Q': 'What are the responsibilities of a Product Owner in Scrum?', 'A': 'The Product Owner is responsible for maximizing the value of the product and the work of the Development Team. This includes defining product features, prioritizing the Product Backlog, and ensuring that the backlog is visible, transparent, and clear to all.'},
        {'Q': 'What are the responsibilities of a Scrum Master?', 'A': 'The Scrum Master is responsible for ensuring that Scrum is understood and enacted. This involves coaching the team, facilitating Scrum events, removing impediments, and promoting an environment for high performance and continuous improvement.'},
        {'Q': 'What are the responsibilities of the Development Team in Scrum?', 'A': 'The Development Team is responsible for delivering potentially shippable increments of the product at the end of each Sprint. They are self-organizing and cross-functional, meaning they have all the skills necessary to create a product increment.'},

        # Scrum Framework: Events
        {'Q': 'What is Sprint Planning in Scrum?', 'A': 'Sprint Planning is an event in Scrum that marks the beginning of a Sprint. During this meeting, the Product Owner, Scrum Master, and Development Team collaborate to define the Sprint Goal, select items from the Product Backlog for the Sprint Backlog, and create a plan for delivering the product increment.'},
        {'Q': 'What is a Daily Stand-up (Daily Scrum)?', 'A': 'The Daily Stand-up is a short, time-boxed event that occurs every day of the Sprint. The Development Team members discuss what they did yesterday, what they plan to do today, and any impediments they are facing. It helps to synchronize activities and create a plan for the next 24 hours.'},
        {'Q': 'What is the purpose of a Sprint Review?', 'A': 'The Sprint Review is an event at the end of the Sprint where the Scrum Team and stakeholders inspect the increment and adapt the Product Backlog if needed. It is an opportunity to gather feedback and ensure that the product is progressing in the right direction.'},
        {'Q': 'What is a Sprint Retrospective?', 'A': 'The Sprint Retrospective is an event that occurs at the end of each Sprint. The Scrum Team reflects on the past Sprint to identify and implement improvements. It focuses on what went well, what didn’t, and what actions can be taken to improve the next Sprint.'},

        # Scrum Framework: Artifacts
        {'Q': 'What is a Product Backlog?', 'A': 'The Product Backlog is an ordered list of everything that is known to be needed in the product. It is dynamic and evolves as new requirements, fixes, and improvements are identified. The Product Owner is responsible for maintaining the Product Backlog.'},
        {'Q': 'What is a Sprint Backlog?', 'A': 'The Sprint Backlog is a list of tasks and user stories that the Development Team selects for completion during a Sprint. It includes a plan for delivering the product increment and is updated daily to reflect the current status of the work.'},
        {'Q': 'What is an Increment in Scrum?', 'A': 'An Increment is the sum of all the Product Backlog items completed during a Sprint, plus the value of the increments of all previous Sprints. It must be in a usable condition, meeting the Scrum Team’s definition of "Done".'},

        # Kanban
        {'Q': 'What is Kanban?', 'A': 'Kanban is a visual management method for optimizing the flow of work. It uses a Kanban Board to visualize the workflow, manage work in progress (WIP), and improve efficiency.'},
        {'Q': 'What is a Kanban Board?', 'A': 'A Kanban Board is a tool used in Kanban to visualize the flow of work. It typically consists of columns representing different stages of the workflow, such as "To Do", "In Progress", and "Done". Tasks are represented by cards that move through the columns as they progress.'},
        {'Q': 'What are WIP Limits in Kanban?', 'A': 'WIP (Work In Progress) Limits are constraints on the number of tasks that can be in a particular stage of the workflow at any time. They help to identify bottlenecks and ensure a smooth flow of work by preventing overloading of work stages.'},

        # Agile Tools
        {'Q': 'What is Jira and how is it used in Agile?', 'A': 'Jira is a project management tool developed by Atlassian. It is widely used in Agile methodologies to plan, track, and manage software development projects. Jira supports Scrum and Kanban boards, backlog management, sprint planning, and reporting.'},
        {'Q': 'What are Azure DevOps Boards?', 'A': 'Azure DevOps Boards are a suite of Agile tools provided by Microsoft Azure to support planning, tracking, and discussing work across teams. They include Kanban boards, backlogs, team dashboards, and custom reporting.'},
        {'Q': 'How do you use Jira for Sprint Planning?', 'A': 'In Jira, Sprint Planning involves creating a sprint in a Scrum board, adding issues from the Product Backlog to the Sprint Backlog, setting the Sprint Goal, and estimating tasks. The sprint is then started, and the Development Team works on completing the tasks.'},
        {'Q': 'What are some common Agile metrics tracked in Jira?', 'A': 'Common Agile metrics tracked in Jira include Velocity (amount of work completed in a sprint), Burndown Chart (work remaining in the sprint), and Cycle Time (time taken to complete a task). These metrics help to measure team performance and project progress.'},
        # Jira Basics
        {'Q': 'What is Jira?', 'A': 'Jira is a project management tool developed by Atlassian that is widely used for issue tracking, bug tracking, and project management. It supports Agile methodologies, including Scrum and Kanban.'},
        {'Q': 'How do you create a new project in Jira?', 'A': 'To create a new project in Jira, you navigate to the Projects dropdown, select Create Project, choose a project template (e.g., Scrum, Kanban), configure the project settings, and click Create.'},

        # Jira Tickets and Workflows
        {'Q': 'What is an issue in Jira?', 'A': 'An issue in Jira is a single work item or task that needs to be tracked and managed. Issues can be of different types, such as bugs, tasks, stories, and epics.'},
        {'Q': 'How do you create an issue in Jira?', 'A': 'To create an issue in Jira, you click the Create button, fill in the issue details such as project, issue type, summary, description, assignee, and priority, and then click Create.'},
        {'Q': 'What are workflows in Jira?', 'A': 'Workflows in Jira define the sequence of statuses and transitions that an issue goes through during its lifecycle. They can be customized to match the specific processes of a team or project.'},
        {'Q': 'How do you configure workflows in Jira?', 'A': 'To configure workflows in Jira, you go to the Jira administration area, select Issues, then Workflows. You can create new workflows, edit existing ones, add statuses, transitions, and conditions.'},
        {'Q': 'What is a transition in a Jira workflow?', 'A': 'A transition in a Jira workflow is the action that moves an issue from one status to another. Transitions can have conditions, validators, and post-functions.'},
        {'Q': 'How do you add custom fields to Jira issues?', 'A': 'To add custom fields to Jira issues, you navigate to the Jira administration area, select Issues, then Custom Fields. You can create new custom fields and add them to the appropriate screens and field configurations.'},
        {'Q': 'What are issue types in Jira?', 'A': 'Issue types in Jira represent different kinds of work items, such as bugs, tasks, stories, epics, and sub-tasks. Each issue type can have its own workflow, screen, and field configuration.'},
        
        # Jira Boards and Backlogs
        {'Q': 'What is a Scrum board in Jira?', 'A': 'A Scrum board in Jira is a visual representation of the work to be done in a sprint. It includes columns for different statuses, such as To Do, In Progress, and Done, and allows teams to track the progress of their sprint tasks.'},
        {'Q': 'What is a Kanban board in Jira?', 'A': 'A Kanban board in Jira is a visual tool that represents the flow of work. It includes columns for different stages of the workflow, such as Backlog, Selected for Development, In Progress, and Done, and helps teams manage work in progress and optimize flow.'},
        {'Q': 'What is a backlog in Jira?', 'A': 'A backlog in Jira is a list of work items (issues) that are prioritized and ready to be taken up by the team. In a Scrum project, the backlog is managed and refined during sprint planning and backlog grooming sessions.'},
        
        # Jira Reports and Dashboards
        {'Q': 'What are some common reports available in Jira?', 'A': 'Common reports in Jira include the Burndown Chart, Velocity Chart, Sprint Report, Control Chart, and Cumulative Flow Diagram. These reports help teams track progress, measure performance, and identify bottlenecks.'},
        {'Q': 'How do you create a dashboard in Jira?', 'A': 'To create a dashboard in Jira, you go to the Dashboards menu, select Create Dashboard, provide a name and description, and add gadgets that display various metrics and reports. Dashboards can be customized and shared with team members.'},
        {'Q': 'What is the Burndown Chart in Jira?', 'A': 'The Burndown Chart in Jira is a graphical representation of the work remaining versus time. It helps teams track the progress of a sprint and predict whether the sprint goal will be achieved.'},

        # Pipelines and CI/CD
        {'Q': 'What is a CI/CD pipeline?', 'A': 'A CI/CD pipeline is a series of automated processes that allow developers to build, test, and deploy code changes continuously. CI stands for Continuous Integration, and CD stands for Continuous Deployment or Continuous Delivery.'},
        {'Q': 'How do you set up a CI/CD pipeline?', 'A': 'To set up a CI/CD pipeline, you need a version control system (e.g., Git), a CI/CD tool (e.g., Jenkins, Azure Pipelines, GitLab CI), and a set of scripts or configuration files that define the build, test, and deployment processes. The pipeline is triggered by code changes pushed to the repository.'},
        {'Q': 'What is Jenkins and how is it used in CI/CD?', 'A': 'Jenkins is an open-source automation server that is widely used for implementing CI/CD pipelines. It provides plugins for integrating with various version control systems, build tools, and deployment platforms. Jenkins can be configured to automate the entire software delivery process.'},
        {'Q': 'What are Azure Pipelines?', 'A': 'Azure Pipelines is a cloud-based CI/CD service provided by Azure DevOps. It supports building, testing, and deploying applications to various environments. Azure Pipelines integrates with GitHub, Azure Repos, and other Git repositories.'},
        {'Q': 'What are the key components of a CI/CD pipeline?', 'A': 'Key components of a CI/CD pipeline include source code repository, build server, testing framework, deployment scripts, and monitoring tools. These components work together to ensure that code changes are automatically tested and deployed to production.'},
        {'Q': 'How do you handle pipeline failures?', 'A': 'Pipeline failures are handled by implementing proper error handling, notifications, and rollback mechanisms. When a failure occurs, the pipeline should provide detailed logs and alerts to the development team, who can then investigate and fix the issue.'},

        # Use Cases and Best Practices
        {'Q': 'How do you manage code quality in a CI/CD pipeline?', 'A': 'Code quality in a CI/CD pipeline is managed by incorporating static code analysis, unit tests, integration tests, and code reviews into the pipeline. Tools like SonarQube can be used to perform code analysis and generate quality reports.'},
        {'Q': 'What are the best practices for creating and managing Jira tickets?', 'A': 'Best practices for creating and managing Jira tickets include providing clear and concise descriptions, setting appropriate priorities, linking related issues, using labels and components for categorization, and regularly updating the status and details of the tickets.'},
        {'Q': 'How do you handle dependencies between Jira tickets?', 'A': 'Dependencies between Jira tickets are managed using issue links. You can create links such as "blocks", "is blocked by", "relates to", etc. This helps to visualize and manage the relationships between different work items.'},
        {'Q': 'What are some common use cases for Jira in Agile development?', 'A': 'Common use cases for Jira in Agile development include managing product backlogs, planning sprints, tracking sprint progress, conducting retrospectives, and generating reports for performance measurement and process improvement.'},
        {'Q': 'How do you integrate Jira with other tools in a DevOps pipeline?', 'A': 'Jira can be integrated with other tools in a DevOps pipeline using plugins, APIs, and webhooks. Common integrations include version control systems (e.g., Git), CI/CD tools (e.g., Jenkins, Azure Pipelines), and collaboration tools (e.g., Slack, Microsoft Teams).'}
    ],
    'Azure': [
        # Core Azure Services: Compute
        {'Q': 'What are Azure Virtual Machines (VMs)?', 'A': 'Azure Virtual Machines are on-demand, scalable computing resources that provide a way to run virtualized applications and workloads.'},
        {'Q': 'What are Azure App Services?', 'A': 'Azure App Services are fully managed platform-as-a-service (PaaS) offerings that enable you to build, deploy, and scale web apps and APIs quickly.'},
        {'Q': 'What are Azure Functions?', 'A': 'Azure Functions is a serverless compute service that allows you to run event-driven code without managing infrastructure. It supports a variety of programming languages and can be triggered by various events.'},

        # Core Azure Services: Storage
        {'Q': 'What is Azure Blob Storage?', 'A': 'Azure Blob Storage is a service for storing large amounts of unstructured data, such as text or binary data. It is highly scalable and durable.'},
        {'Q': 'What is Azure Table Storage?', 'A': 'Azure Table Storage is a NoSQL key-value store for rapid development using massive semi-structured datasets. It is a part of Azure Storage.'},
        {'Q': 'What is Azure Queue Storage?', 'A': 'Azure Queue Storage is a service for storing large numbers of messages that can be accessed from anywhere via authenticated calls using HTTP or HTTPS.'},

        # Core Azure Services: Databases
        {'Q': 'What is Azure SQL Database?', 'A': 'Azure SQL Database is a fully managed relational database service built on SQL Server technologies, providing high availability, scalability, and security.'},
        {'Q': 'What is Azure Cosmos DB?', 'A': 'Azure Cosmos DB is a globally distributed, multi-model database service that provides horizontal scalability and guaranteed low-latency access to data.'},

        # Core Azure Services: Networking
        {'Q': 'What is an Azure Virtual Network (VNet)?', 'A': 'An Azure Virtual Network (VNet) is a logically isolated network in Azure that allows you to securely connect Azure resources to each other and to on-premises networks.'},
        {'Q': 'What are Azure Load Balancers?', 'A': 'Azure Load Balancers distribute incoming network traffic across multiple virtual machines, ensuring high availability and reliability of applications.'},
        {'Q': 'What is Azure DNS?', 'A': 'Azure DNS is a hosting service for DNS domains that provides name resolution using Microsoft Azure infrastructure. It allows you to manage your DNS records using the same credentials and billing as your other Azure services.'},

        # Azure DevOps
        {'Q': 'What are Azure DevOps Boards?', 'A': 'Azure DevOps Boards provide a suite of Agile tools to support planning and tracking work, code defects, and issues using Kanban and Scrum methods.'},
        {'Q': 'What are Azure DevOps Repos?', 'A': 'Azure DevOps Repos provide Git repositories or Team Foundation Version Control (TFVC) for source control of your code.'},
        {'Q': 'What are Azure DevOps Pipelines?', 'A': 'Azure DevOps Pipelines are cloud-hosted pipelines for fast CI/CD that work with any language, platform, and cloud. They enable you to build, test, and deploy applications.'},
        {'Q': 'What are Azure DevOps Test Plans?', 'A': 'Azure DevOps Test Plans provide a rich set of tools to test your applications, including manual/exploratory testing and continuous testing as part of your CI/CD pipeline.'},
        {'Q': 'What are Azure DevOps Artifacts?', 'A': 'Azure DevOps Artifacts is an extension to Azure DevOps Services and Azure DevOps Server which allows you to create, host, and share packages with your team.'},

        # Azure Resource Manager (ARM) Templates
        {'Q': 'What are Azure Resource Manager (ARM) Templates?', 'A': 'ARM Templates are JSON files that define the infrastructure and configuration for your Azure solution. They enable you to deploy, manage, and configure all the resources for your solution in a declarative way.'},

        # Azure Identity and Access Management (IAM)
        {'Q': 'What is Azure Active Directory (Azure AD)?', 'A': 'Azure Active Directory is a cloud-based identity and access management service. It helps your employees sign in and access resources in external resources, such as Microsoft 365, the Azure portal, and thousands of other SaaS applications.'},
        {'Q': 'What is Role-Based Access Control (RBAC) in Azure?', 'A': 'RBAC is an authorization system built on Azure Resource Manager that provides fine-grained access management of Azure resources. It allows you to assign permissions to users, groups, and applications at a certain scope.'},

        # Monitoring and Logging
        {'Q': 'What is Azure Monitor?', 'A': 'Azure Monitor is a service that provides a complete solution for collecting, analyzing, and acting on telemetry from your cloud and on-premises environments. It helps you understand how your applications are performing and proactively identify issues affecting them.'},
        {'Q': 'What is Application Insights?', 'A': 'Application Insights is a feature of Azure Monitor that provides extensible application performance management (APM) and monitoring for live web applications. It helps you detect and diagnose performance issues and understand usage patterns.'},

        # Security
        {'Q': 'What is Azure Key Vault?', 'A': 'Azure Key Vault is a cloud service that provides secure storage and management of sensitive information such as keys, secrets, and certificates. It helps you control access to these sensitive data and simplifies their management.'},
        {'Q': 'What is Azure Security Center?', 'A': 'Azure Security Center is a unified infrastructure security management system that strengthens the security posture of your data centers and provides advanced threat protection across your hybrid workloads in the cloud.'},

        # Deployment Models
        {'Q': 'What are ARM Templates and how are they used in deployment?', 'A': 'ARM Templates are used to define the infrastructure and configuration for your Azure solution in a declarative JSON format. They are used in deployment to ensure consistency and repeatability of your resources.'},
        {'Q': 'What is Azure CLI and how is it used?', 'A': 'Azure CLI is a cross-platform command-line tool used to manage Azure resources. It allows you to execute commands to create, update, and delete Azure resources from your terminal or command prompt.'},
        {'Q': 'What is the Azure Portal?', 'A': 'The Azure Portal is a web-based application that allows you to build, manage, and monitor everything from simple web apps to complex cloud applications in a single, unified console.'}
    ]
}
