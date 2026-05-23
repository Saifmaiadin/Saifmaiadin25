-- جدول الفروع والمصانع (هيكل شجري)
CREATE TABLE branches (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(20) CHECK (type IN ('branch', 'factory', 'headquarters')),
    parent_branch_id INTEGER REFERENCES branches(id), -- للهيكل الهرمي
    location TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- جدول الأقسام (داخل كل فرع أو مصنع)
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    branch_id INTEGER REFERENCES branches(id) ON DELETE CASCADE
);

-- جدول الموظفين
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    employee_code VARCHAR(20) UNIQUE,
    department_id INTEGER REFERENCES departments(id),
    job_title VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    hire_date DATE,
    salary NUMERIC(12,2),
    status VARCHAR(20) DEFAULT 'active'
);

-- جدول المستخدمين (للدخول إلى النظام)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER UNIQUE REFERENCES employees(id) ON DELETE CASCADE,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL, -- استخدم bcrypt
    is_active BOOLEAN DEFAULT true
);

-- جدول الأدوار (مثل: مدير فرع، محاسب، مشرف مصنع)
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    scope VARCHAR(20) CHECK (scope IN ('global', 'branch', 'department'))
);

-- جدول صلاحيات الوصول (لكل دور، لكل كيان)
CREATE TABLE permissions (
    id SERIAL PRIMARY KEY,
    role_id INTEGER REFERENCES roles(id),
    resource VARCHAR(50), -- مثلاً 'employees', 'products', 'financials'
    action VARCHAR(20),   -- 'view', 'create', 'edit', 'delete'
    branch_id INTEGER REFERENCES branches(id) NULL -- NULL يعني كل الفروع
);

-- ربط المستخدم بالأدوار
CREATE TABLE user_roles (
    user_id INTEGER REFERENCES users(id),
    role_id INTEGER REFERENCES roles(id),
    PRIMARY KEY (user_id, role_id)
);